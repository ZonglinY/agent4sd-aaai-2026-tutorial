---
layout: page
use-site-title: false
---

<h1 style="font-size: 60px; text-align: center;">Agentic AI for Scientific Discovery: Benchmarks, Frameworks, and Applications</h1>

<style>
  /* Speakers layout: predictable, centered, wraps cleanly */
  .speakers {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 24px;               /* space between cards */
    text-align: center;
  }

  /* Neutralize Bootstrap floats in this section only */
  .speakers > [class*="col-"] {
    float: none !important;
    padding: 0;
    flex: 0 1 240px;   /* was 300px, now smaller */
  }

  /* Card: vertical stack */
  .speaker-card {
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* Photo */
  .speaker-photo {
    width: 220px;
    height: 220px;
    object-fit: contain;     
    object-position: center;
    border-radius: 50%;
    background-color: #fff;
    display: block;
    margin-bottom: 12px;
  }





  /* Name */
  .speaker-name {
    display: block;
    font-weight: 600;
    margin: 6px 0 2px;
    line-height: 1.3;
  }

  /* Note under speaker name (e.g., representing Xinya Du) */
  .speaker-note {
    display: block;
    margin: 0 0 4px;
    line-height: 1.2;
    font-size: 0.92em;
    color: #777;
  }

  /* Affiliation — reserve up to 3 lines so cards align */
  .speaker-affil {
    display: block;
    line-height: 1.35;
    min-height: 4.05em;      /* ≈ 3 lines; use 2.7em for 2 lines */
    word-break: break-word;
    overflow-wrap: anywhere;
    color: #555;
  }
</style>





<!--<div class="venue" style="font-size: 24px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  <span style="font-size: 23px; font-weight: 300;">
    <a target="_blank" href="https://drive.google.com/file/d/1oTRnVPSqrHoJb5xcu3cQ0_Jtflpj4bqW/view?usp=sharing">[Slides]</a>
  </span>
</div>-->



<div class="sharethis-inline-share-buttons"></div>
<meta name="thumbnail" content="./img/aaai-logo.png" />

<div class="container" style="margin-bottom: 10px;"></div>


<!-- Speakers -->
<!--<div class="container text-center" style="margin-top:25px;margin-bottom:40px;">
  <div class="row speakers">
    {% for p in site.data.organizers %}
      {% assign person = p[1] %}
      <div class="col-xs-12 col-sm-6 col-md-4">
        <div class="speaker-card">
          <img class="speaker-photo"
               src="{{ site.baseurl }}/img/{{ person.img }}"
               alt="{{ person.name }}"
               loading="lazy">
          <a class="speaker-name" href="{{ person.url }}" target="_blank" rel="noopener">{{ person.name }}</a>
          <small class="speaker-affil">{{ person.affiliation }}</small>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
<hr>-->

<!-- Speakers -->
<div class="container text-center" style="margin-top:25px;margin-bottom:40px;">
  <div class="row speakers">
    {% for p in site.data.organizers %}
      {% assign person = p[1] %}
      <div class="col-xs-12 col-sm-6 col-md-4">
        <div class="speaker-card">
          <img class="speaker-photo"
               src="{{ site.baseurl }}/img/{{ person.img }}"
               alt="{{ person.name }}"
               loading="lazy">

          <a class="speaker-name"
             href="{{ person.url }}"
             target="_blank"
             rel="noopener">
            {{ person.name }}
          </a>

          {% if person.note %}
            <small class="speaker-note">({{ person.note }})</small>
          {% endif %}

          <small class="speaker-affil">{{ person.affiliation }}</small>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
<hr>





<!-- # Program Committee
<div class="container">
  <ul class="list-group list-group-flush">
    {% for p in site.data.pc.people %}
      <li class="list-group-item col-xs-6 col-sm-4 col-md-3">{{ p }}</li>
    {% endfor %}
  </ul>
</div>
<hr> -->


<!-- <div class="tutorial-slides">
  <h2>Slides</h2>
  <ul>
    <li><a href="https://github.com/ZonglinY/llm4sd-aaai-2026/blob/main/_data/AAAI26-Agents-Tutorial-Reddy.pptx" target="_blank">Part 1: by Chandan Reddy</a></li>
    <li><a href="https://docs.google.com/presentation/d/1n92tzyFGcDAsQG4uZ_jIGQV39jgCrEAP/edit?usp=sharing&ouid=111093169629314886898&rtpof=true&sd=true" target="_blank">Part 2: by Zonglin Yang</a></li>
    <li><a href="https://docs.google.com/presentation/d/1Ek-mPEpsjlvNbk7U9xp1o1G0NwE-x_Mu0E7M_5zILq8/edit?usp=sharing" target="_blank">Part 3: by Ruochen Li</a></li>
  </ul>
</div> -->

<div class="tutorial-slides">
  <h2>Slides</h2>
  <ul>
    <li><a href="https://github.com/ZonglinY/llm4sd-aaai-2026/blob/main/_data/AAAI26-Agents-Tutorial-Reddy.pptx?raw=true">Part 1: by Chandan Reddy</a></li>
    <li><a href="https://github.com/ZonglinY/agent4sd-aaai-2026-tutorial/blob/main/_data/AAAI-Tutorial-Zonglin.pptx?raw=true">Part 2: by Zonglin Yang</a></li>
    <li><a href="https://docs.google.com/presentation/d/1Ek-mPEpsjlvNbk7U9xp1o1G0NwE-x_Mu0E7M_5zILq8/edit?usp=sharing" target="_blank">Part 3: by Ruochen Li</a></li>
  </ul>
</div>






# Detailed Tutorial Description

## Overview
The rise of large language models (LLMs) has introduced a paradigm shift in how AI can contribute to science. Beyond serving as static predictors, LLMs can function as agents that actively generate, refine, and evaluate hypotheses. This tutorial provides a structured overview of how agentic AI can accelerate the scientific discovery process, grounded in recent advances in benchmarks, frameworks, and applications.

## Motivation
Traditional machine learning excels at prediction but falls short in hypothesis-driven discovery, where novelty, interpretability, and iterative reasoning are essential. The promise of agentic AI lies in closing this gap. By structuring the discovery process into two complementary phases, we highlight how AI can play an active role in advancing science:

1. **Hypothesis Generation** – AI agents propose candidate hypotheses by retrieving inspirations, composing associations, and ranking them for plausibility.  
2. **Feedback and Refinement** – Hypotheses are iteratively improved using diverse feedback signals, including data fit, reasoning consistency, symbolic decomposition, or benchmark performance.  

This cycle mirrors the way human scientists move from initial ideas to refined, testable hypotheses, but accelerates it through automated reasoning and structured agentic workflows.

## Tutorial Outline
1. **Introduction to Agentic AI in Science**  
   - From prediction to discovery  
   - Defining “agentic AI” and distinguishing it from static LLM use  
   - Motivating examples  

2. **Phase I: Hypothesis Generation**  
   - Inspiration retrieval and knowledge recombination  
   - From qualitative hypotheses to symbolic formulations  
   - Ranking strategies and novelty assessment  

3. **Phase II: Feedback and Refinement**  
   - Iterative optimization using feedback signals  
   - Data-driven evaluation, symbolic decomposition, and reasoning consistency checks  
   - Hierarchical refinement from coarse ideas to fine-grained hypotheses  

4. **Benchmarks for Scientific Discovery**  
   - Limitations of existing datasets (memorization vs reasoning)  
   - Principles for robust benchmark design  
   - Recent benchmarks for equations, hypotheses, and surfaces  

5. **Frameworks for Agentic Discovery**  
   - Decomposition strategies, memory mechanisms, and feedback loops  
   - Integration of evolutionary search and reinforcement learning  
   - Examples of agentic workflows  

6. **Applications Across Sciences**  
   - Social sciences (open-domain hypothesis generation)  
   - Natural sciences (equation discovery, symbolic modeling)  
   - Broader applications in AI for science  

7. **Challenges and Future Directions**  
   - Reliability, interpretability, reproducibility  
   - Balancing creativity and validity  
   - Toward hybrid AI–science collaborations  

## Target Audience
Researchers and practitioners in machine learning, NLP, and AI for science who are interested in symbolic reasoning, agentic frameworks, and automated discovery. The tutorial is accessible to those with general familiarity with LLMs and does not require deep domain expertise.

## Learning Outcomes
Participants will gain:
- An understanding of the two-phase cycle of agentic scientific discovery.  
- Exposure to recent benchmarks for evaluating reasoning beyond memorization.  
- Insight into frameworks that integrate decomposition, evolutionary search, and feedback mechanisms.  
- Awareness of applications across disciplines and the challenges they expose.  
- A forward-looking perspective on building reliable, interpretable science-focused agents.  


<!--This tutorial presents a structured overview of how large language models (LLMs) can accelerate the **cycle of scientific discovery**, divided into two phases: the **pre-experiment phase**, which focuses on **search and optimization guided by LLMs’ internal heuristics**, and the **experiment-guided phase**, which emphasizes **optimization with experimental feedback**. Together, these phases illustrate how LLMs can drive a **complete discovery cycle**, moving from hypothesis formulation to experimental impact.  

In the **pre-experiment phase**, the central question is: *How are scientific hypotheses fundamentally formulated?* Directly generating valid hypotheses from background knowledge is intractable. A key advance was to introduce a **foundational equation** that decomposes this challenge into tractable subtasks: retrieving inspirations, composing hypotheses, and ranking them. This provides a principled basis for **exploratory discovery**. Yet most generated hypotheses remain **coarse-grained**, too vague to guide experiments. To address this gap, researchers have introduced the task of **fine-grained hypothesis discovery**, which requires producing hypotheses with detailed methodological and experimental specifications. This task has been shown to have **combinatorial optimization complexity**, as it involves selecting coherent details from a vast space of possibilities. A hierarchical optimization strategy mitigates this complexity by progressively refining hypotheses across levels of abstraction, effectively **smoothing the hypothesis search landscape** and enabling more reliable convergence toward testable outcomes.  

In the **experiment-guided phase**, the key challenge is how to harness experimental feedback as a guiding signal. In domains where experimentation is relatively **efficient**, **symbolic regression (SR)** provides a powerful framework. SR uncovers explicit mathematical equations directly from data, producing models that are both predictive and **interpretable**. Unlike black-box predictors, SR reveals transparent structures that enhance scientific understanding and trust. The tutorial will trace SR’s **foundations and evolution**, from early search-based and evolutionary algorithms to recent AI-driven approaches that integrate deep learning and large language models. We will discuss how these approaches expand the expressiveness and scalability of SR, enabling it to discover equations in increasingly complex settings. Special attention will be given to **evaluation and benchmarking**: what makes an equation scientifically meaningful, how interpretability can be measured alongside accuracy, and how benchmarks can be designed to reflect discovery goals. Finally, we highlight SR’s **practical impact** across physics, biology, and engineering, where interpretable equations validate hypotheses and generate new insights.  

When experiments are **costly and resource-intensive**, the challenge shifts to prioritization: only a few hypotheses can be tested, and AI can help rank candidates and direct scarce resources toward the most promising directions.  

By structuring discovery into these two phases—**optimization with heuristics before experiments, and optimization with experimental feedback**—this tutorial provides a **complete cycle** for **LLM-assisted scientific discovery**.  -->



<hr>


# Reading List

## Introduction

- [Towards Scientific Discovery with Generative AI: Progress, Opportunities, and Challenges (AAAI'25)](https://creddy.net/papers/AAAI25.pdf)
- [A Survey on Large Language Models for Scientific Research](https://arxiv.org/abs/2501.04306)
- [Transformer-Based Planning for Symbolic Regression (NeurIPS'23)](https://creddy.net/papers/NeurIPS23a.pdf)
- [SNIP: Bridging Mathematical Symbolic and Numeric Realms with Unified Pre-training (ICLR'24)](https://creddy.net/papers/ICLR24.pdf)
- [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567)
- [LLM-FE: Automated Feature Engineering for Tabular Data with LLMs as Evolutionary Optimizers](https://arxiv.org/abs/2503.14434)


## Pre-experiment Phase

- [Large Language Models for Automated Open-domain Scientific Hypotheses Discovery (ACL'24)](https://arxiv.org/abs/2309.02726) 
- [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses (ICLR'25)](https://arxiv.org/abs/2410.07076) 
- [MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery via Hierarchical Search (NeurIPS'25)](https://arxiv.org/abs/2505.19209) 
- [MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier](https://arxiv.org/abs/2603.03756)
- [ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](https://arxiv.org/abs/2503.21248)


## Experiment-guided Phase (Efficient Experimentation)

- [LLM-SR: Scientific Equation Discovery via Programming with Large Language Models (ICLR'25 Oral)](https://creddy.net/papers/ICLR25.pdf)
- [LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models (ICML'25 Oral)](https://creddy.net/papers/ICML25.pdf)
- [Data-Efficient Symbolic Regression via Foundation Model Distillation](https://arxiv.org/abs/2508.19487)
- [SURFACEBENCH: Can Self-Evolving LLMs Find the Equations of 3D Scientific Surfaces?](https://arxiv.org/abs/2511.10833)
- [Decompose, Adapt, and Evolve: Towards Efficient Scientific Equation Discovery with Large Language Models (NeurIPS'25 Mathematical Reasoning and AI workshop)](https://openreview.net/forum?id=lbwWQg4q8A)



## Experiment-guided Phase (Costly Experimentation)
- [MOOSE-Chem3: Toward Experiment-Guided Hypothesis Ranking via Simulated Experimental Feedback (NeurIPS'25 AI4S workshop)](https://arxiv.org/abs/2505.17873) 
- [Accelerating Materials Design via LLM-Guided Evolutionary Search](https://arxiv.org/abs/2510.22503)
- [Mlr-copilot: Autonomous machine learning research based on large language models agents](https://arxiv.org/abs/2408.14033)
- [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://arxiv.org/abs/2506.17335)
- [Learning to Generate Research Idea with Dynamic Control (AAAI'25 AI4Research workshop)](https://openreview.net/forum?id=zCb0dPvGYN)

<hr>

<!--# Symbolic Regression Taxonomy

credit: [Symbolic Regression Tutorial](https://symbolicregression2025.github.io/)

![Taxonomy-viz](./img/taxonomy.jpg)-->
