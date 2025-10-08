---
#layout: archive
permalink: /projects/
author_profile: true
---



<div class="recent_updates" style="margin-top:30px; font-size:32px;">Projects</div>

<style>
  /* Subheading style */
  .sub_heading {
    font-weight: 700;
    font-size: 28px;
    margin-top: 30px;
    margin-bottom: 15px;
    text-align: left;
    color: #2c3e50;
    border-left: 5px solid #a115a0;
    padding-left: 10px;
  }

  /* Project card */
  .project-card {
    background-color: #f9f9f9;
    border-radius: 12px;
    padding: 20px 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(159, 155, 214, 0.93);
  }

  .project-title {
    font-size: 22px;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 8px;
  }

  /* .project-tags {
    font-size: 14px;
    color: #fff;
    background-color: #a115a0;
    padding: 3px 8px;
    border-radius: 5px;
    margin-right: 5px;
    display: inline-block;
    margin-bottom: 10px;
  } */

  .project-tags {
  font-size: 14px;
  color: #333;
  background-color: #e4d8ee; /* pale lilac */
  padding: 3px 8px;
  border-radius: 5px;
  margin-right: 5px;
  display: inline-block;
  margin-bottom: 10px;
}

  .project-text {
    font-size: 15px;
    line-height: 1.6em;
    color: #333;
    margin-bottom: 12px;
  }

  .project-text a.tab_paper {
  display: inline-block;
  background: linear-gradient(135deg, #bba4e3, #c9b6ec); /* soft lilac gradient */
  color: #fff;
  padding: 6px 12px;
  border-radius: 6px;
  margin-right: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.25s ease;
  box-shadow: 0 2px 6px rgba(187, 164, 227, 0.4);
}

.project-text a.tab_paper:hover {
  background: linear-gradient(135deg, #a985e9, #c79ee8); /* slightly richer hover */
  box-shadow: 0 4px 10px rgba(169, 133, 233, 0.5);
  transform: translateY(-2px);
}
/* 

  .project-text a.tab_paper {
    display: inline-block;
    background-color:rgba(159, 155, 214, 0.93) #afbdf5ff;
    color: #fff;
    padding: 6px 12px;
    border-radius: 6px;
    margin-right: 8px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.2s ease;
  }
  .project-text a.tab_paper:hover {
    background-color: #e08ce9ff;
  } */
</style>

<div class="sub_heading">Robotics Projects</div>

<div class="project-card">
  <div class="project-title">Klann Mechanism</div>
  <span class="project-tags">Mechanism Design</span>
  <p class="project-text">
    Designed and simulated a Klann linkage mechanism to replicate legged locomotion using a six-bar linkage system.
    <br><br>
    <a target="_blank" class="tab_paper" href="https://github.com/yourusername/klann-mechanism">Code</a>
    <a target="_blank" class="tab_paper" href="https://iiithydresearch-my.sharepoint.com/:p:/g/personal/shreya_bollimuntha_research_iiit_ac_in/EQVsGRQuhVFDsP3tfNkVm9wBOm5G-yeFYun7OkPFT8wzCw?e=cdbcKs">Presentation</a>
    <a target="_blank" class="tab_paper" href="/Projects/MSD/Techamronics_Presentation.pptx">Presentation</a>
  </p>
</div>


<div class="project-card">
  <div class="project-title">Pose Graph Optimization for 2D SLAM</div>
  <span class="project-tags">SLAM</span>
  <span class="project-tags">Optimization</span>
  <span class="project-tags">Python</span>
  <span class="project-tags">g2o</span>
  <div class="project-text">
    Developed a pose graph-based 2D Simultaneous Localization and Mapping (SLAM) system using nonlinear least squares optimization, integrating odometric and loop closure constraints to significantly improve robot trajectory accuracy. Utilized Python and libraries such as NumPy and g2o for algorithm implementation and performance evaluation against ground truth data.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/icp-slam-the-ro-bots">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Stereo Dense Reconstruction</div>
  <span class="project-tags">3D Vision</span>
  <span class="project-tags">OpenCV</span>
  <span class="project-tags">Open3D</span>
  <span class="project-tags">Depth Estimation</span>
  <div class="project-text">
    Developed a dense 3D reconstruction pipeline using OpenCV's SGBM algorithm to compute disparity maps from stereo images, generating detailed colored point clouds with Open3D for autonomous robotic scene understanding.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/stereo-dense-reconstruction-the-ro-bots">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Camera–IMU Calibration</div>
  <span class="project-tags">Sensor Fusion</span>
  <span class="project-tags">ROS2</span>
  <span class="project-tags">RealSense</span>
  <span class="project-tags">Calibration</span>
  <div class="project-text">
    Developed a precise camera–IMU calibration pipeline using ROS2 and Intel RealSense sensors to estimate extrinsic parameters, achieving low MSE in orientation estimation and enabling accurate sensor fusion for motion tracking.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Ro-Bots/tree/main/imu-camera-callibration-the-ro-bots">Code</a>
  </div>
</div>

<div class="sub_heading">AI & ML Projects</div>

<div class="project-card">
  <div class="project-title">Megathon – Social Media Personality Analysis</div>
  <span class="project-tags">Android</span>
  <span class="project-tags">NLP</span>
  <span class="project-tags">Psychometrics</span>
  <div class="project-text">
    Developed an Android app that analyzes social media activity and psychometric test results to classify users as better suited for tech or sales roles. The app outputs a percentage match for each category, aiding recruiters in shortlisting candidates.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Social-Media-Personality-Analysis">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Movie Recommender System</div>
  <span class="project-tags">Collaborative Filtering</span>
  <span class="project-tags">Machine Learning</span>
  <span class="project-tags">Python</span>
  <div class="project-text">
    Built a movie recommender system using collaborative filtering and matrix factorization methods to provide personalized movie suggestions based on user ratings and preferences.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Recommender-Systems">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Precog – Election Classification</div>
  <span class="project-tags">Text Classification</span>
  <span class="project-tags">NLP</span>
  <span class="project-tags">Machine Learning</span>
  <div class="project-text">
    Implemented a classification model to categorize election-related social media posts, contributing to large-scale political discourse analysis under the Precog research group.  
    <a target="_blank" class="tab_paper" href="https://github.com/bollimuntha-shreya/Election-Classification">Code</a>
  </div>
</div>

<div class="project-card">
  <div class="project-title">Precog – Election Spends Project</div>
  <span class="project-tags">Data Analysis</span>
  <span class="project-tags">Computer Vision</span>
  <span class="project-tags">NLP</span>
  <div class="project-text">
    Worked on analyzing and classifying election-related advertisement data to estimate campaign expenditures, using text and image-based analysis pipelines.  
    <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/Election-Ads/">Code 1</a>
    <a target="_blank" class="tab_paper" href="https://github.com/harsha20032020/ElectionsSpendsProject">Code 2</a>
  </div>
</div>

