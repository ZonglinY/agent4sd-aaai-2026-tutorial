/* Optional browser QA: install playwright and axe-core outside the site or expose
   them through NODE_PATH. Usage: node scripts/browser_check.cjs https://agent4sd.io */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const base = (process.argv[2] || 'http://127.0.0.1:8765').replace(/\/$/, '');
const output = process.env.QA_OUTPUT || '/tmp/tutorial-site-qa';
fs.mkdirSync(output, { recursive: true });
(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chromium.executablePath(), args: ['--no-sandbox']});
  const page = await browser.newPage();
  const errors = [], results = [];
  page.setDefaultNavigationTimeout(60000);
  // Do not invoke the historical page's third-party sharing tracker during QA.
  await page.route('https://platform-api.sharethis.com/**', route => route.abort());
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => {
    if (response.url().startsWith(base + '/') && response.status() >= 400 && !response.url().endsWith('/favicon.ico')) errors.push(`${response.status()} ${response.url()}`);
  });
  for (const width of [1440, 768, 390, 320]) {
    await page.setViewportSize({width, height: 1000});
    for (const route of ['/', '/list/', '/2027/', '/2026/', '/404.html']) {
      const response = await page.goto(base + route, {waitUntil: 'networkidle'});
      if (response.status() !== 200) throw Error(`HTTP ${response.status()}: ${route}`);
      await page.locator('img').evaluateAll(images => Promise.all(images.map(image => { image.loading = 'eager'; return image.decode().catch(() => {}); })));
      const dimensions = await page.evaluate(() => ({width: innerWidth, scroll: document.documentElement.scrollWidth, brokenImages: [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.src)}));
      if (dimensions.scroll > width + 1 || dimensions.brokenImages.length) throw Error(JSON.stringify({route, ...dimensions}));
      if (['/', '/2027/'].includes(route)) {
        if (await page.locator('.schedule').count()) throw Error('Timetable still present');
        if (!await page.getByRole('heading', {name: 'Detailed Tutorial Description', exact: true}).count()) throw Error('Missing tutorial structure');
      }
      results.push({route, ...dimensions});
      if (width === 1440 || width === 390) {
        const name = route === '/' ? 'home' : route.split('/')[1];
        await page.screenshot({path: path.join(output, `${name}-${width}.png`), fullPage: true});
        await page.screenshot({path: path.join(output, `${name}-${width}-viewport.png`)});
      }
    }
  }
  await page.setViewportSize({width: 1440, height: 1000});
  await page.goto(base + '/');
  const homeText = await page.locator('main').innerText();
  await page.goto(base + '/2027/');
  if (homeText !== await page.locator('main').innerText()) throw Error('Home/latest content mismatch');
  await page.getByRole('link', {name: 'All editions', exact: true}).first().click();
  await page.waitForURL(base + '/list/');
  await page.getByRole('link', {name: 'Explore AAAI 2027', exact: false}).click();
  await page.waitForURL(base + '/2027/');
  await page.getByRole('link', {name: '← All tutorials', exact: true}).click();
  await page.waitForURL(base + '/list/');
  await page.getByRole('link', {name: 'Visit the archive', exact: false}).click();
  await page.waitForURL(base + '/2026/');
  await page.getByRole('link', {name: '← All tutorials', exact: true}).click();
  await page.waitForURL(base + '/list/');
  await page.goto(base + '/#reading-list');
  if (!page.url().endsWith('/#reading-list')) throw Error('Latest-page anchor redirected');
  await page.goto(base + '/2027/');
  await page.getByText('Biography of Dianbo Liu', {exact: true}).click();
  if (await page.locator('.speaker details').first().getAttribute('open') === null) throw Error('Biography did not open');
  const accessibility = [];
  for (const width of [1440, 390]) {
    await page.setViewportSize({width, height: 1000});
    for (const route of ['/', '/list/', '/2027/', '/404.html']) {
      await page.goto(base + route);
      await page.addScriptTag({path: require.resolve('axe-core/axe.min.js')});
      const violations = await page.evaluate(async () => (await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa']}})).violations.map(v => ({id: v.id, nodes: v.nodes.map(n => n.target)})));
      accessibility.push({route, width, violations});
      if (violations.length) errors.push(JSON.stringify({route, width, violations}));
    }
  }
  const nojs = await browser.newContext({javaScriptEnabled: false});
  const plain = await nojs.newPage();
  await plain.goto(base + '/');
  if (await plain.locator('.speaker').count() !== 4) throw Error('Missing no-JS content');
  await nojs.close();
  await browser.close();
  fs.writeFileSync(path.join(output, 'results.json'), JSON.stringify({base, results, accessibility, errors}, null, 2));
  if (errors.length) throw Error(errors.join('\n'));
  console.log(JSON.stringify({result: 'PASS', base, responsiveChecks: results.length, accessibilityChecks: accessibility.length, errors}));
})().catch(error => {console.error(error); process.exit(1);});
