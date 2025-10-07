---
permalink: /
#layout: archive
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div hidden="hidden">
<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=P0DmcjPhTVQDSVsO6eLpfLlblpD7aYEdFi8dEehI1TI&cl=ffffff&w=a"></script>
</div>
<h3>About Me</h3>

<span class="small_font">
I am a robotics researcher and an aspiring PhD candidate, currently in my final year of Dual Degree (B Tech and Master of Science in Electronics and Communication Engineering by Research) at IIIT Hyderabad. My research is centered on developing intelligent robotic systems that can learn complex manipulation tasks.
<br><br>
At the Robotics Research Centre (RRC), I have had the privilege of working under the guidance of  
Prof. <a target="_blank" href="https://www.iiit.ac.in/people/faculty/mkrishna/">K. Madhava Krishna</a> and Prof. <a target="_blank" href="https://nagamanigi.wixsite.com/home">Nagamanikandan Govindan</a>. My work is focused around dual arm manipulation, with publications accepted at major conferences like ICRA and IROS.
<br><br>
Beyond robotics, I have gained experience in software engineering as an intern at Stripe, where I developed an anomaly detection system, and have explored applied machine learning through various projects. I am driven by the goal of creating autonomous systems that can robustly perform meaningful tasks in the real world.
<br><br>
<!-- Outside the lab, music plays a significant role in my life. I am a Grade 7 certified pianist from Trinity College of Music London and have represented my institution in various inter-college music competitions. I find that the discipline and creativity required in music complement my technical work in unexpected ways. When not immersed in research or playing piano, I love traveling and exploring new places. Experiencing different cultures broadens my perspective and fuels my curiosity. -->
Outside the lab, I lead a balanced life filled with music and sports. I am a Grade 7 certified pianist from Trinity College of Music London and have competed in various inter-college music competitions. I'm also an active participant in sports, having won competitions in both basketball and swimming. I find that the discipline from music and the teamwork from sports complement my technical work in unexpected ways. When not immersed in research, playing piano, or on the court, I love traveling and exploring new places. Experiencing different cultures broadens my perspective and fuels my curiosity.
</span>

<h3>Research Interests</h3>
<span class="small_font">
My research interest lies in enabling robots to master complex, real-world manipulation tasks with the fluidity and adaptability of humans. I am particularly drawn to the intersection of reinforcement learning, control theory, and optimization. My goal is to develop algorithms that allow robots, especially in dual-arm settings, to learn efficiently by leveraging underlying physical and kinematic models. I believe the future of robotics hinges not just on collecting massive datasets, but on creating sample-efficient learning frameworks that can reason about contact, dynamics, and collaboration to solve tasks that are currently beyond their reach.
</span>


<div class="recent_updates">Publications</div>

<span style="font-size:14px;margin-bottom: -25px;display: block;">*Equal Contribution <!--/ <span class="highlight">Highlighted Papers</span>--></span>

<div class="research-block">
  <div class="left">
		<span class="research-img">
			<img src="/papers/DAVIL_teaser.gif">
		</span>
	</div>
  <div class="right">
    <div class="title">DA-VIL: Adaptive Dual-Arm Manipulation with Reinforcement Learning and Variable Impedance Control</div>
    <div class="sub-title"><i><b>ICRA 2025</b></i><br>
    Md Faizal Karim*, <b style="color:#a115a0">Shreya Bollimuntha</b>*, Mohammed Saad Hashmi, Autrio Das, Gaurav Singh, Srinath Sridhar, Arun Kumar Singh, Nagamanikandan Govindan, K Madhava Krishna<br>
	<a target="_blank" class="tab_paper" target="_blank" href="https://ieeexplore.ieee.org/abstract/document/11127487">Paper</a><a target="_blank"  class="tab_paper" href="https://dualarmvil.github.io/Dual-Arm-VIL/">Code</a><a target="_blank"  class="tab_paper" href="https://dualarmvil.github.io/Dual-Arm-VIL/">Website</a>
    </div>
  </div>
</div>

<div class="research-block">
  <div class="left">
		<span class="research-img">
			<img src="/papers/DG16M_teaser.gif">
		</span>
	</div>
  <div class="right">
    <div class="title">DG16M: A Large-Scale Dataset for Dual-Arm Grasping with Force-Optimized Grasps</div>
    <div class="sub-title"><i><b>ICRA 2025</b></i><br>
    Md Faizal Karim*, <b style="color:#a115a0">Shreya Bollimuntha</b>*, Mohammed Saad Hashmi, Autrio Das, Gaurav Singh, Srinath Sridhar, Arun Kumar Singh, Nagamanikandan Govindan, K Madhava Krishna<br>
    <a target="_blank" class="tab_paper" target="_blank" href="https://arxiv.org/abs/2503.08358">Paper</a><a target="_blank"  class="tab_paper" href="https://github.com/DG16M/DG16M-dataset">Code</a><a target="_blank"  class="tab_paper" href="https://dg16m.github.io/DG-16M/">Website</a>
    </div>
  </div>
</div>

<div class="research-block">
<div class="left">
		<span class="research-img">
			<img src="/papers/DART_teaser.gif">
		</span>
	</div>
  <div class="right">
    <div class="title">DART: Learning-Enhanced Model Predictive Control for Dual-Arm Non-Prehensile Manipulation</div>
     <div class="sub-title"><i><b>Under Review</b></i><br>
    <a target="_blank" class="tab_paper" target="_blank" href="./papers/ICRA26_3775_MS.pdf">Paper</a><a target="_blank"  class="tab_paper" href="https://github.com/dart-icra/DART-Dual-Arm-Non-Prehensile-Manipulation">Code</a><a target="_blank"  class="tab_paper" href="https://dart-icra.github.io/dart/">Website</a>
  </div>
</div>

<style>
  .recent_updates {
    font-weight: 600;
    font-size: 20px;
    margin-bottom: 6px;
  }

  .updates {
    list-style: none;
    padding-left: 0;
    margin-top: -3px;
  }

  .updates li {
    margin-bottom: 8px;
    line-height: 1.5em;
    display: flex;
    align-items: flex-start;        /* keep items top-aligned */
    justify-content: flex-start;    /* ensure left alignment */
  }

  .updates-month {
    min-width: 70px;
    font-weight: bold;
    color: #555;
    display: inline-block;
    text-align: left;
  }

  .updates-content {
    flex: 1;
    display: block;
    text-align: left;               /* <-- ensures content is left-aligned */
    word-wrap: break-word;
  }

  .updates img {
    vertical-align: middle;
  }
</style>



<div class="recent_updates">News and Announcements</div>
 <ul style="margin-top:-3px" class="updates">
	<!-- <li><span class="updates-month">JUL '24</span> <span class="updates-content">"Constrained 6-DoF Grasp Generation on Complex Shapes for Improved Dual-Arm Manipulation" accepted at <b>IROS 2024</b>!</span></li>
	<li><span class="updates-month">JAN '24</span> <span class="updates-content">2 papers accepted at <b>ICRA 2024</b>!</span></li>
	<li><span class="updates-month">NOV '23</span> <span class="updates-content">Presented "EDMP: Ensemble-of-costs-guided Diffusion for Motion Planning" at <b>CoRL Workshop 2023</b><a target="_blank" href="https://sites.google.com/view/corl2023-prl/home"><img src="/images/link.png" width=18px height=18px style="margin: -7px 5px 0 5px;"></a>!</span></li> -->

  <!-- <li><span class="updates-month">OCT '25</span> <span class="updates-content">Presented "DG16M: A Large-Scale Dataset for Dual-Arm Grasping with Force-Optimized Grasps" at <b>IROS 2025</b> in Hangzhou, China.</span></li> -->
  <li><span class="updates-month">JUL '25</span> <span class="updates-content">Completed internship at <a target="_blank" href="https://stripe.com/in">Stripe</a>! Invited for a Friday Fireside Chat with John and Patrick Collison to present my work done at the internship.</span></li>
	<li><span class="updates-month">JUN '25</span> <span class="updates-content">"DG16M: A Large-Scale Dataset for Dual-Arm Grasping with Force-Optimized Grasps" accepted at <b>IROS 2025</b><a target="_blank" href="https://dg16m.github.io/DG-16M/"><img src="/images/link.png" width=18px height=18px style="margin: -7px 5px 0 5px;"></a>!🎉</span></li>
  <li><span class="updates-month">MAY '25</span> <span class="updates-content">Presented "DA-VIL: Adaptive Dual-Arm Manipulation with Reinforcement Learning and Variable Impedance Control" at <b>ICRA 2025</b> in Atlanta, USA.</span></li>
  <li><span class="updates-month">MAY '25</span> <span class="updates-content">Started internship at <a target="_blank" href="https://stripe.com/in">Stripe</a>!</span></li>
	<li><span class="updates-month">APR '25</span> <span class="updates-content">Served as reviewer for <a target="_blank" href="https://2025.ieee-icra.org/">ICRA 2025</a>.</span></li>
	<li><span class="updates-month">JAN '25</span> <span class="updates-content">"DA-VIL: Adaptive Dual-Arm Manipulation with Reinforcement Learning and Variable Impedance Control" accepted for presentation at <b>ICRA 2025</b><a target="_blank" href="https://dualarmvil.github.io/Dual-Arm-VIL/"><img src="/images/link.png" width=18px height=18px style="margin: -7px 5px 0 5px;"></a>!🎉</span></li>
</ul>


<style>
  .project-block {
    display: flex;
    align-items: flex-start;
    margin-bottom: 25px;
  }

  .project-block .left {
    flex: 0 0 220px;
    margin-right: 20px;
  }

  .project-block .left img {
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .project-block .right {
    flex: 1;
  }

  .project-block .title {
    font-weight: 600;
    font-size: 17px;
    margin-bottom: 6px;
  }

  .project-block .sub-title {
    color: #333;
    line-height: 1.6em;
    text-align: left;
  }
</style>



<div class="recent_updates" style="margin-top:30px;">Projects</div>

<div class="project-block">
  <div class="left">
    <span class="project-img">
      <img src="/images/posegraph.png" alt="Pose Graph Optimization">
    </span>
  </div>
  <div class="right">
    <div class="title">Pose Graph Optimization for 2D SLAM</div>
    <div class="sub-title">
      Developed a pose graph-based <b>2D SLAM</b> system using nonlinear least squares optimization, integrating odometric and loop closure constraints to significantly improve robot trajectory accuracy.<br><br>
      Utilized <b>Python</b> and libraries such as <b>NumPy</b> and <b>g2o</b> for algorithm implementation and evaluation against ground truth data.
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/icp-slam-the-ro-bots">Code</a>
    </div>
  </div>
</div>



<div class="project-block">
  <div class="left">
    <span class="project-img">
      <img src="/images/posegraph.png" alt="Stereo Dense Reconstruction">
    </span>
  </div>
  <div class="right">
    <div class="title">Stereo Dense Reconstruction</div>
    <div class="sub-title">
      Developed a dense 3D reconstruction pipeline by applying OpenCV’s Semi-Global Block Matching (SGBM) algorithm to compute accurate disparity maps from rectified stereo image pairs. Leveraged camera calibration parameters and Open3D to generate and visualize detailed colored point clouds, enhancing scene understanding for autonomous robotic applications.
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/stereo-dense-reconstruction-the-ro-bots">Code</a>
    </div>
  </div>
</div>

<div class="project-block">
  <div class="left">
    <span class="project-img">
      <img src="/images/posegraph.png" alt="Camera-IMU Calibration">
    </span>
  </div>
  <div class="right">
    <div class="title">Camera-IMU Calibration</div>
    <div class="sub-title">
      Developed a precise calibration pipeline for synchronizing Intel RealSense camera and IMU sensors using ROS2, enabling accurate sensor fusion for enhanced motion tracking and environmental perception.
      Implemented calibration algorithms to estimate extrinsic parameters, achieving low mean squared error (MSE) in orientation estimation and ensuring reliable alignment between camera and IMU data streams.
      <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/imu-camera-callibration-the-ro-bots">Code</a>
    </div>
  </div>
</div>






<!-- <div class="research-block">
	<div class="left">
		<span class="research-img">
			<img src="/images/teasers/personalized.gif">
		</span>
	</div>
	<div class="right">
		<div class="title">Personalized One-Shot Lipreading for an ALS Patient</div>
		<div class="sub-title"><b style="color:#a115a0">Bipasha Sen</b>*, Aditya Agarwal*, Rudrabha Mukhopadhyay, Vinay Namboodiri, C V Jawahar <i><br><b>BMVC 2021</b></i><a class="tab_paper" target="_blank" href="https://www.bmvc2021-virtualconference.com/assets/papers/1468.pdf">paper</a><a target="_blank"  class="tab_paper" href="https://youtu.be/_famGVaem-8">video</a><a target="_blank"  class="tab_paper" href="http://bhaasha.iiit.ac.in/lipwav">portal</a></div>
		<span class="research-text">
		We propose a personalized network to lipread an ALS patient using only one-shot examples. Our approach significantly improves and achieves high top-5accuracy with 83.2% accuracy compared to 62.6% achieved by comparable methods for the patient. Apart from evaluating our approach on the ALS patient, we also extend it to people with hearing impairment relying extensively on lip movements to communicate.
		</span>
	</div>
</div> -->

