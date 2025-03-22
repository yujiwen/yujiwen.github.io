---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
Hi, I'm Jiwen. I am a first-year Ph.D. student at The University of Hong Kong (HKU), supervised by Prof. [Xihui Liu](https://xh-liu.github.io/). Currently, I also work as a research intern at Kuaishou Technology under the guidance of Dr. [Xintao Wang](https://xinntao.github.io/). Prior to this, I received my Master's degree from Peking University, where I was supervised by Prof. [Jian Zhang](https://jianzhang.tech/). My research interests cover generative models and embodied AI, with a particular focus on physical and virtual applications of video generation models.

I am always open to academic and industrial collaborations. My specific research interests include:

- **Development of foundational video generation models** (autoregressive models, causal inference, and efficient architectures)
- **Video generation models as world simulators** (generalization, physics-compliance, memory consistency, and causal reasoning)
- **Multi-agent embodied AI**

Feel free to reach out for research discussions and potential collaborations!

<span class='anchor' id='publications'></span>
# Selected Publications 

(*: indicates equal contribution; #: indicates corresponding author)

## Current Research Topics: Video Generation Model / World Model / Embodied AI

Video generation models learn world knowledge from large-scale video data, showing promise in simulating the physical world and even synthesizing novel virtual worlds. I envision video generation models evolving into comprehensive world simulators, with applications spanning gaming, embodied AI, and beyond.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper/gamefactory.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**GameFactory: Creating New Games with Generative Interactive Videos**

<u><strong>Jiwen Yu</strong></u><sup>*</sup>, Yiran Qin<sup>*</sup>, Xintao Wang<sup>#</sup>, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>

Preprint, 2025

[**Paper**](https://arxiv.org/pdf/2501.08325) **|** [**Project Page**](https://yujiwen.github.io/gamefactory/) **|** [**GitHub**](https://github.com/KwaiVGI/GameFactory) **|** [**Dataset**](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper/igv_position.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Position: Interactive Generative Video as Next-Generation Game Engine**

<u><strong>Jiwen Yu</strong></u><sup>*</sup>, Yiran Qin<sup>*</sup>, Haoxuan Che, Quande Liu, Xintao Wang<sup>#</sup>, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>

Preprint, 2025

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/paper/worldsimbench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**WorldSimBench: Towards Video Generation Models as World Simulators**

Yiran Qin<sup>*</sup>, Zhelun Shi<sup>*</sup>, <u><strong>Jiwen Yu</strong></u>, Xijun Wang, Enshen Zhou, Lijun Li, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao, Lei Bai, Wanli Ouyang, Ruimao Zhang

Preprint, 2024

[**Paper**](https://arxiv.org/pdf/2410.18072) **|** [**Project Page**](https://iranqin.github.io/WorldSimBench.github.io/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='/images/paper/skillmimic.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SkillMimic: Learning Reusable Basketball Skills from Demonstrations**

Yinhuai Wang<sup>*</sup>, Qihan Zhao<sup>*</sup>, Runyi Yu<sup>*</sup>, Ailing Zeng, Jing Lin, Zhengyi Luo, Hok Wai Tsui, <u><strong>Jiwen Yu</strong></u>, Xiu Li, Qifeng Chen, Jian Zhang, Lei Zhang, Ping Tan

CVPR, 2025

[**Paper**](https://arxiv.org/abs/2408.15270) **|** [**Project Page**](https://ingrid789.github.io/SkillMimic/) **|** [**GitHub**](https://github.com/wyhuai/SkillMimic)
</div>
</div>

## Early Research Topic: Training-free Applications of Diffusion Model

My research journey began during my Master's studies, coinciding with the paradigm shift brought by diffusion models in generative AI (2021-2023). This revolutionary advancement inspired my initial research on zero-shot applications of diffusion models, spanning multiple domains including image restoration, generation, editing, steganography, and video synthesis.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Project</div><img src='/images/paper/animatezero.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**AnimateZero: Video Diffusion Models are Zero-Shot Image Animators**

<u><strong>Jiwen Yu</strong></u><sup></sup>, Xiaodong Cun<sup>#</sup>, Chenyang Qi, Yong Zhang, Xintao Wang, Ying Shan, Jian Zhang<sup>#</sup>

Project, 2023

[**Paper**](https://arxiv.org/abs/2312.03793) **|** [**Project Page**](https://yujiwen.github.io/animatezero.github.io/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='/images/paper/cross.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CRoSS: Diffusion Model Makes Controllable, Robust and Secure Image Steganography**

<u><strong>Jiwen Yu</strong></u>, Xuanyu Zhang, Youmin Xu, Jian Zhang<sup>#</sup>

NeurIPS, 2023

[**Paper**](https://arxiv.org/abs/2305.16936) **|** [**GitHub**](https://github.com/yujiwen/CRoSS)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2023</div><img src='/images/paper/freedom.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model**

<u><strong>Jiwen Yu</strong></u>, Yinhuai Wang, Chen Zhao<sup>#</sup>, Bernard Ghanem, Jian Zhang<sup>#</sup>

ICCV, 2023

[**Paper**](https://arxiv.org/abs/2303.09833) **|** [**GitHub**](https://github.com/yujiwen/FreeDoM)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR, 2023</div><img src='/images/paper/ddnm.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Zero-Shot Image Restoration Using Denoising Diffusion Null-Space Model**


Yinhuai Wang<sup>*</sup>, <u><strong>Jiwen Yu</strong></u><sup>*</sup>, Jian Zhang<sup>#</sup>

ICLR, 2023

[**Paper**](https://arxiv.org/pdf/2212.00490) **|** [**GitHub**](https://github.com/wyhuai/DDNM) **|** [**Project Page**](https://wyhuai.github.io/ddnm.io/)
</div>
</div>


<span class='anchor' id='educations'></span>
# Educations

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/hku.jpg" alt="HKU Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2024.09 - Now</strong></p>
        <p>Ph.D. Student, <a href="https://www.hku.hk/">University of Hong Kong</a>, HKU-<a href="https://mmlab.ie.cuhk.edu.hk/">MMLab</a></p>
        <p>Advisor: Prof. <a href="https://xh-liu.github.io/">Xihui Liu</a></p>
    </div>
</div>

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/pku.svg.png" alt="Peking University Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2021.09 - 2024.06</strong></p>
        <p>M.S., <a href="https://english.pku.edu.cn/">Peking University</a>, <a href="https://villa.jianzhang.tech/">VILLA Lab</a></p>
        <p>Advisor: Prof. <a href="https://jianzhang.tech/">Jian Zhang</a></p>
    </div>
</div>



<span class='anchor' id='internships'></span>
# Internships

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/kuaishou.png" alt="Kuaishou Technology Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2024.09 - Now</strong></p>
        <p>Research Intern at KwaiVGI, <a href="https://www.kuaishou.com/">Kuaishou Technology</a>, Shenzhen, China</p>
        <p>Advisor: Dr. <a href="https://xinntao.github.io/">Xintao Wang</a></p>
    </div>
</div>

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/tencent_ai_lab.png" alt="Tencent AI Lab Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2023.04 - 2024.01</strong></p>
        <p>Research Intern at <a href="https://ailab.tencent.com/ailab/en/index/">Tencent AI Lab</a>, Shenzhen, China</p>
        <p>Advisor: Prof. <a href="https://vinthony.github.io/academic/">Xiaodong Cun</a></p>
    </div>
</div>


<span class='anchor' id='service'></span>
# Academic Service
- Reviewer, [ICLR](https://iclr.cc/), [NeurIPS](https://neurips.cc/), [ICML](https://icml.cc/), [ECCV](https://eccv.ecva.net/), [CVPR](https://cvpr.thecvf.com/), [ICCV](https://iccv.thecvf.com/), [SIGGRAPH](https://www.siggraph.org/).