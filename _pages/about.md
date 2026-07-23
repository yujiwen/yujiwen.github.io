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
Hi, I'm **Jiwen**, a researcher and frontier explorer in generative AI.

I'm building <span style="font-family: 'Orbitron', sans-serif; font-weight: 600; letter-spacing: 2px; background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff); background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradientShift 4s ease infinite;">Video World Model</span>: AI systems that generate consistent, controllable video environments with real-time interactivity, memory, and reasoning capabilities. As [Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) and [Project Genie](https://labs.google/projectgenie?utm_source=deepmind.google&utm_medium=referral&utm_campaign=gdm&utm_content=) have shown, this is the foundation for next-generation simulation, robotics, and interactive media, yet there's still a long way to go.

🤗 I'm fortunate to have [Yiran Qin](https://iranqin.github.io/) as a close friend and collaborator. We share a deep interest in the intersection of world models and robotics.

🤝 <strong>Open to collaborations</strong> from academia, industry, or investment. If you're interested in video world models, let's talk!

<span style="display: inline-block; margin-top: 10px; padding: 8px 16px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 6px;">
  <span style="color: #fff; font-size: 0.9em;">
    Contact me via 📬 
    <a href="#" onclick="event.preventDefault(); document.getElementById('email-modal').style.display='block';" style="color: #fff; text-decoration: underline;">Email</a> 
    / 
    <a href="#" onclick="event.preventDefault(); document.getElementById('wechat-qr').style.display='block';" style="color: #fff; text-decoration: underline;">WeChat</a>
  </span>
</span>
<a href="https://scholar.google.com.hk/citations?user=uoRPLHIAAAAJ" target="_blank" style="display: inline-block; margin-top: 10px; margin-left: 8px; padding: 8px 16px; background: linear-gradient(135deg, #4285F4 0%, #0F9D58 100%); border-radius: 6px; text-decoration: none; vertical-align: top;">
  <span style="color: #fff; font-size: 0.9em;">🎓 Google Scholar Citations: <strong id="total_cit">2442</strong></span>
</a>

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
    <p style="margin-top:12px; color:#555; font-size:1em;">Please tell me your name and affiliation (current or past) when adding my wechat. Thanks!</p>
  </div>
</div>

<span class='anchor' id='research-vision'></span>
# Research Vision

My long-term research goal is to build ideal <span style="font-family: 'Orbitron', sans-serif; font-weight: 600; letter-spacing: 2px; background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff); background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradientShift 4s ease infinite;">Video World Model</span>. I'm currently focused on three core challenges:

<div style="margin: 12px 0; padding: 12px 18px; background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(0,255,136,0.08)); border-left: 4px solid #00d4ff; border-radius: 8px;">
⚡ <strong>Real-Time Streaming Generation.</strong> Generating high-quality streaming video with interactive control and memory, which requires substantial engineering and infrastructure work beyond algorithms alone.
</div>

<div style="margin: 12px 0; padding: 12px 18px; background: linear-gradient(135deg, rgba(102,126,234,0.08), rgba(118,75,162,0.08)); border-left: 4px solid #764ba2; border-radius: 8px;">
🧠 <strong>Memory Systems.</strong> Building complex, comprehensive memory architectures that integrate diverse tools (context, 3D representations, learnable parameters, etc.) and support a wide range of functions including retrieval, querying, compression, and updates.
</div>

<div style="margin: 12px 0; padding: 12px 18px; background: linear-gradient(135deg, rgba(255,165,0,0.08), rgba(255,69,0,0.08)); border-left: 4px solid #ff8c00; border-radius: 8px;">
👁️ <strong>Visual Intelligence.</strong> Can large-scale video training alone give rise to advanced intelligence? Not short-term dynamics prediction, but long-horizon analysis, reasoning, and planning. I believe video data holds great potential for emergent capabilities.
</div>

<!-- <p align="center">
  <img src="images/paper/long_term_goal.jpg" alt="My Long Term Research Goal" width="1000"><br>
</p> -->


<span class='anchor' id='publications'></span>
# Selected Publications 

(*: indicates equal contribution; #: indicates corresponding author)

## Research Topics: World Model / Interactive Video Generation / Embodied AI

<!-- Video generation models learn world knowledge from large-scale video data, showing promise in simulating the physical world and even synthesizing novel virtual worlds. I envision video generation models evolving into comprehensive world simulators, with applications spanning gaming, embodied AI, and beyond. -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><video src='videos/MemLearner.mp4' autoplay loop muted playsinline width="100%"></video></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>MemLearner: Learning to Query Context Memory for Video World Models</strong></span>

<u><strong>Jiwen Yu</strong></u>, Jianxiong Gao, Jianhong Bai, Yiran Qin, Kaiyi Huang, Quande Liu, Xintao Wang<sup>#</sup>, Pengfei Wan, Kun Gai, Xihui Liu<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">ECCV 2026</span>

[**Paper**](https://arxiv.org/pdf/2606.31734) **|** [**Project Page**](https://yujiwen.github.io/memlearner/)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SIGGRAPH Asia 2025</div><video src='videos/CaM.mp4' autoplay loop muted playsinline width="100%"></video></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval</strong></span>

<u><strong>Jiwen Yu</strong></u><sup></sup>, Jianhong Bai, Yiran Qin, Quande Liu<sup>#</sup>, Xintao Wang, Pengfei Wan, Di Zhang, Xihui Liu<sup>#</sup>

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">SIGGRAPH Asia 2025</span>

[**Paper**](https://arxiv.org/pdf/2506.03141) **|** [**Project Page**](https://context-as-memory.github.io/) **|** [**Dataset**](https://huggingface.co/datasets/KwaiVGI/Context-as-Memory-Dataset)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><video src='videos/GameFactory.mp4' autoplay loop muted playsinline width="100%"></video></div></div>
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


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPRW 2026</div><video src='videos/multiworld.mp4' autoplay loop muted playsinline width="100%"></video></div></div>
<div class='paper-box-text' markdown="1">

<span style="font-size:1.3em;"><strong>MultiWorld: Scalable Multi-Agent Multi-View Video World Models</strong></span>

Haoyu Wu, <u><strong>Jiwen Yu</strong></u>, Yingtian Zou, Xihui Liu

<span style="background-color: #fff9c4; color: #333; padding: 2px 8px; border-radius: 6px; font-weight: bold;">CVPR 2026 Workshop MARS-EAI <span style="color: #e74c3c; font-weight: bold;">Best Paper Award</span></span>

[**Paper**](https://arxiv.org/pdf/2604.18564) **|** [**Project Page**](https://multi-world.github.io/)
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
        <img src="images/logo/anuttacon_logo.jpg" alt="Anuttacon Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2026.01 - 2026.06</strong></p>
        <p>Student Researcher at <a href="https://www.anuttacon.com/about/">Anuttacon</a>, Mountain View, CA, US</p>
        <p>Advisor: Dr. <a href="https://scholar.google.com/citations?user=P91a-UQAAAAJ&hl=en">Xin Tong</a></p>
    </div>
</div>

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/kuaishou.png" alt="Kuaishou Technology Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2024.09 - 2026.01</strong></p>
        <p>Student Researcher (Kuai Star) at <a href="https://klingai.com/">Kling</a> team, Shenzhen, China</p>
        <p>Advisor: Dr. <a href="https://xinntao.github.io/">Xintao Wang</a></p>
    </div>
</div>

<div class="experience-box">
    <div class="experience-box-logo">
        <img src="images/logo/tencent_ai_lab.png" alt="Tencent AI Lab Logo">
    </div>
    <div class="experience-box-text">
        <p><strong>2023.04 - 2024.01</strong></p>
        <p>Student Researcher at <a href="https://ailab.tencent.com/ailab/en/index/">Tencent AI Lab</a>, Shenzhen, China</p>
        <p>Advisor: Prof. <a href="https://vinthony.github.io/academic/">Xiaodong Cun</a></p>
    </div>
</div>

<span class='anchor' id='talks'></span>
# Talks

- <span style="background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,255,136,0.1)); padding: 2px 8px; border-radius: 4px; font-size: 0.85em; color: #555;">Jul 2026</span> **Interactive Video Generation towards World Models**
  - F2S Workshop @ ICML 2026. [[Workshop]](https://icml2026-f2s-workshop.github.io/)

- <span style="background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,255,136,0.1)); padding: 2px 8px; border-radius: 4px; font-size: 0.85em; color: #555;">Dec 2025</span> **Controllable, Generalizable, and Memory-Enabled: Interactive Video World Models**
  - SAAI. [[News Report]](https://mp.weixin.qq.com/s/v5QRFAu5SeodanhqeX1e8Q) (Chinese)

- <span style="background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,255,136,0.1)); padding: 2px 8px; border-radius: 4px; font-size: 0.85em; color: #555;">Dec 2025</span> **Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval**
  - GAMES. [[Video]](https://www.bilibili.com/video/BV1WnmCByEnT) (Chinese)

- <span style="background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,255,136,0.1)); padding: 2px 8px; border-radius: 4px; font-size: 0.85em; color: #555;">Oct 2025</span> **Toward Higher-Level Intelligence in Interactive Generative Video for World Model**
  - AITIME. [[Video]](https://www.bilibili.com/video/BV1uu4wzuE4B) (Chinese)

- <span style="background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,255,136,0.1)); padding: 2px 8px; border-radius: 4px; font-size: 0.85em; color: #555;">Jul 2025</span> **Toward Higher-Level Intelligence of Interactive Generative Video**
  - TechBeat. [[Video]](https://www.bilibili.com/video/BV1cy8kzEEtQ/) (Chinese)

<span class='anchor' id='service'></span>
# Academic Service and Honors
- Invited Outstanding Student Speaker at VALSE 2026 Outstanding Student Forum [[News Report]](https://mp.weixin.qq.com/s/muATsaDvIJb2LcrtcXm8Tg) (Chinese)
- Primary Organizer, [VideoWorldModel](https://videoworldmodel-workshop.github.io/) (CVPR'26 Workshop)
- Reviewer, [ICLR](https://iclr.cc/), [NeurIPS](https://neurips.cc/), [ICML](https://icml.cc/), [ECCV](https://eccv.ecva.net/), [CVPR](https://cvpr.thecvf.com/), [ICCV](https://iccv.thecvf.com/), [SIGGRAPH](https://www.siggraph.org/), [SIGGRAPH Asia](https://asia.siggraph.org/), [TPAMI](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34).

<div style="margin: 20px 0; padding: 20px 24px; background: linear-gradient(135deg, #0a0a0a, #1a1a2e); border-radius: 12px; border: 1px solid rgba(0,212,255,0.3); position: relative; overflow: hidden;">
  <div style="position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff); background-size: 200% 100%; animation: gradientShift 4s ease infinite;"></div>
  <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 10px;">
    <span style="font-family: 'Orbitron', sans-serif; font-weight: 600; font-size: 1.1em; letter-spacing: 2px; background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff); background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradientShift 4s ease infinite;">VideoWorldModel</span>
    <span style="background: rgba(0,212,255,0.15); color: #00d4ff; padding: 2px 10px; border-radius: 20px; font-size: 0.78em; font-weight: 500; letter-spacing: 0.5px;">CVPR 2026 Workshop</span>
  </div>
  <p style="color: #ccc; font-size: 0.92em; margin: 0 0 12px 0; line-height: 1.6;">
    I served as a Primary Organizer of the <strong style="color: #fff;">Video World Models</strong> workshop at CVPR 2026. The workshop has now concluded — you can revisit the program and accepted works on the workshop website.
  </p>
  <a href="https://videoworldmodel-workshop.github.io/" target="_blank" style="display: inline-block; padding: 7px 20px; border: 1px solid #00d4ff; color: #00d4ff; border-radius: 6px; font-size: 0.85em; font-weight: 500; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.background='#00d4ff';this.style.color='#0a0a0a'" onmouseout="this.style.background='transparent';this.style.color='#00d4ff'">View Recap →</a>
</div>