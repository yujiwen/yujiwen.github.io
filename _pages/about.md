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
Hi, I'm Jiwen. I am a first-year Ph.D. student at The University of Hong Kong (HKU), supervised by Prof. [Xihui Liu](https://xh-liu.github.io/). Currently, I also work as a research intern at [Kling](https://klingai.com/) team of Kuaishou Technology under the guidance of Dr. [Xintao Wang](https://xinntao.github.io/), working closely with my friend [Yiran Qin](https://iranqin.github.io/). Prior to this, I received my Master's degree from Peking University, where I was supervised by Prof. [Jian Zhang](https://jianzhang.tech/). My research interests cover generative models and embodied AI, with a particular focus on physical and virtual applications of video generation models.

<span class='anchor' id='research highlights'></span>
# Research Highlights

My long-term research goal is to construct foundational world models and apply them in the fields of gaming and Embodied AI. Specifically, my research interests focus on two main aspects: 

- (1) Foundational world model research based on our proposed framework with five modules (as shown in the figure below); 
- (2) The application of world models in Embodied AI. 

I am always open to academic and industrial collaborations, if you share the vision, please do not hesitate to contact me via <a href="#" onclick="event.preventDefault(); document.getElementById('email-modal').style.display='block';">Email</a> or <a href="#" onclick="event.preventDefault(); document.getElementById('wechat-qr').style.display='block';">WeChat</a>.

<!-- Email Modal -->
<div id="email-modal" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.5); z-index:9999; text-align:center;">
  <div style="display:inline-block; margin-top:10vh; background:#fff; padding:24px 24px 12px 24px; border-radius:12px; position:relative;">
    <span style="position:absolute; top:8px; right:16px; font-size:24px; cursor:pointer;" onclick="document.getElementById('email-modal').style.display='none';">&times;</span>
    <p style="margin-bottom:8px;"><strong>My Email Address</strong></p>
    <p style="font-size:1.2em; color:#333; user-select:all;">yujiwen.hk@connect.hku.hk</p>
    <button onclick="navigator.clipboard.writeText('yujiwen.hk@connect.hku.hk')" style="margin-top:8px; padding:4px 12px; border-radius:6px; border:none; background:#f5f5f5; cursor:pointer;">Copy</button>
  </div>
</div>

<!-- WeChat QR Code Modal -->
<div id="wechat-qr" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.5); z-index:9999; text-align:center;">
  <div style="display:inline-block; margin-top:10vh; background:#fff; padding:24px 24px 12px 24px; border-radius:12px; position:relative;">
    <span style="position:absolute; top:8px; right:16px; font-size:24px; cursor:pointer;" onclick="document.getElementById('wechat-qr').style.display='none';">&times;</span>
    <p style="margin-bottom:8px;"><strong>Scan to add me on WeChat</strong></p>
    <img src="images/wechat_qr.jpg" alt="WeChat QR Code" style="width:220px; height:auto; border-radius:8px;">
  </div>
</div>

<p align="center">
  <img src="images/paper/long_term_goal.jpg" alt="My Long Term Research Goal" width="1000"><br>
</p>


<span class='anchor' id='publications'></span>
# Selected Publications 

(*: indicates equal contribution; #: indicates corresponding author)

## Research Topics: Interactive Video Generation / World Model / Embodied AI

<!-- Video generation models learn world knowledge from large-scale video data, showing promise in simulating the physical world and even synthesizing novel virtual worlds. I envision video generation models evolving into comprehensive world simulators, with applications spanning gaming, embodied AI, and beyond. -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SIGGRAPH Asia 2025</div><img src='images/paper/cam.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval</strong></span>

<u><strong>Jiwen Yu</strong></u><sup></sup>, Jianhong Bai, Yiran Qin, Quande Liu<sup>#</sup>, Xintao Wang, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">SIGGRAPH Asia 2025</span>

[**Paper**](https://arxiv.org/pdf/2506.03141) **|** [**Project Page**](https://context-as-memory.github.io/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/paper/gamefactory.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>GameFactory: Creating New Games with Generative Interactive Videos</strong></span>

<u><strong>Jiwen Yu</strong></u><sup>*</sup>, Yiran Qin<sup>*</sup>, Xintao Wang<sup>#</sup>, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">ICCV 2025 <span style="color: #e74c3c; font-weight: bold;">Highlight</span></span>

[**Paper**](https://arxiv.org/pdf/2501.08325) **|** [**Project Page**](https://yujiwen.github.io/gamefactory/) **|** [**GitHub**](https://github.com/KwaiVGI/GameFactory) **|** [**Dataset**](https://huggingface.co/datasets/KwaiVGI/GameFactory-Dataset)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/paper/igv_survey.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">


<span style="font-size:1.3em;"><strong>Survey of Interactive Generative Video</strong></span>

<u><strong>Jiwen Yu</strong></u><sup>*</sup>, Yiran Qin<sup>*</sup>, Haoxuan Che<sup>*</sup>, Quande Liu<sup>#</sup>, Xintao Wang, Pengfei Wan, Di Zhang, Kun Gai, Hao Chen, Xihui Liu<sup>#</sup>  

<span style="font-size:1.3em;"><strong>Position: Interactive Generative Video as Next-Generation Game Engine</strong></span> 

<u><strong>Jiwen Yu</strong></u><sup>*</sup>, Yiran Qin<sup>*</sup>, Haoxuan Che, Quande Liu, Xintao Wang<sup>#</sup>, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>  

[**Survey Paper**](https://arxiv.org/abs/2504.21853) | [**Position Paper**](https://arxiv.org/abs/2503.17359)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='/images/paper/worldsimbench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>WorldSimBench: Towards Video Generation Models as World Simulators</strong></span>

Yiran Qin<sup>*</sup>, Zhelun Shi<sup>*</sup>, <u><strong>Jiwen Yu</strong></u>, Xijun Wang, Enshen Zhou, Lijun Li, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao, Lei Bai, Wanli Ouyang, Ruimao Zhang

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">ICML 2025</span>

[**Paper**](https://arxiv.org/pdf/2410.18072) **|** [**Project Page**](https://iranqin.github.io/WorldSimBench.github.io/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='/images/paper/skillmimic.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>SkillMimic: Learning Reusable Basketball Skills from Demonstrations</strong></span>

Yinhuai Wang<sup>*</sup>, Qihan Zhao<sup>*</sup>, Runyi Yu<sup>*</sup>, Ailing Zeng, Jing Lin, Zhengyi Luo, Hok Wai Tsui, <u><strong>Jiwen Yu</strong></u>, Xiu Li, Qifeng Chen, Jian Zhang, Lei Zhang, Ping Tan

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">CVPR 2025 <span style="color: #e74c3c; font-weight: bold;">Highlight</span></span>

[**Paper**](https://arxiv.org/abs/2408.15270) **|** [**Project Page**](https://ingrid789.github.io/SkillMimic/) **|** [**GitHub**](https://github.com/wyhuai/SkillMimic)
</div>
</div>

## Past Research Topic: Training-free Applications of Diffusion Model

My research journey began during my Master's studies, coinciding with the paradigm shift brought by diffusion models in generative AI (2021-2023). This revolutionary advancement inspired my initial research on zero-shot applications of diffusion models, spanning multiple domains including image restoration, generation, editing, steganography, and video synthesis.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Project</div><img src='/images/paper/animatezero.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>AnimateZero: Video Diffusion Models are Zero-Shot Image Animators</strong></span>

<u><strong>Jiwen Yu</strong></u><sup></sup>, Xiaodong Cun<sup>#</sup>, Chenyang Qi, Yong Zhang, Xintao Wang, Ying Shan, Jian Zhang<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">Project 2023</span>

[**Paper**](https://arxiv.org/abs/2312.03793) **|** [**Project Page**](https://yujiwen.github.io/animatezero.github.io/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='/images/paper/cross.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>CRoSS: Diffusion Model Makes Controllable, Robust and Secure Image Steganography</strong></span>

<u><strong>Jiwen Yu</strong></u>, Xuanyu Zhang, Youmin Xu, Jian Zhang<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">NeurIPS 2023</span>

[**Paper**](https://arxiv.org/abs/2305.16936) **|** [**GitHub**](https://github.com/yujiwen/CRoSS)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2023</div><img src='/images/paper/freedom.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model</strong></span>

<u><strong>Jiwen Yu</strong></u>, Yinhuai Wang, Chen Zhao<sup>#</sup>, Bernard Ghanem, Jian Zhang<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">ICCV 2023</span>

[**Paper**](https://arxiv.org/abs/2303.09833) **|** [**GitHub**](https://github.com/yujiwen/FreeDoM)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR, 2023</div><img src='/images/paper/ddnm.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>Zero-Shot Image Restoration Using Denoising Diffusion Null-Space Model</strong></span>


Yinhuai Wang<sup>*</sup>, <u><strong>Jiwen Yu</strong></u><sup>*</sup>, Jian Zhang<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">ICLR 2023 <span style="color: #e74c3c; font-weight: bold;">Spotlight</span></span>

[**Paper**](https://arxiv.org/pdf/2212.00490) **|** [**GitHub**](https://github.com/wyhuai/DDNM) **|** [**Project Page**](https://wyhuai.github.io/ddnm.io/)
</div>
</div>


<span class='anchor' id='educations'></span>
# Educations

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/HKU.jpg" alt="HKU Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2024.09 - Now</strong></p>
        <p>Ph.D. Student, <a href="https://www.hku.hk/">University of Hong Kong</a>, <a href="https://mmlab.hk/">HKU-MMLab</a></p>
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
        <p>Research Intern at KwaiVGI, <a href="https://www.kuaishou.com/">Kuaishou Technology</a>, <a href="https://klingai.com/">Kling</a> team, Shenzhen, China</p>
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
- Reviewer, [ICLR](https://iclr.cc/), [NeurIPS](https://neurips.cc/), [ICML](https://icml.cc/), [ECCV](https://eccv.ecva.net/), [CVPR](https://cvpr.thecvf.com/), [ICCV](https://iccv.thecvf.com/), [SIGGRAPH](https://www.siggraph.org/), [SIGGRAPH Asia](https://asia.siggraph.org/).