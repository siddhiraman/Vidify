import React from 'react';
import Feature from '../../components/feature/Feature';
import './whatGPT3.css';

const WhatGPT3 = () => (
  <div className="gpt3__whatgpt3 section__margin" id="wgpt3">
    <div className="gpt3__whatgpt3-feature">
      <Feature title="What is VidifyPDF" text="Your brain processes information faster than text. In fact, 90% of information transmitted to the brain is visual, and visuals are processed 60,000X faster than text." />
    </div>
    <div className="gpt3__whatgpt3-heading">
      <h1 className="gradient__text">Why should you convert PDF into Videos?</h1>
     
    </div>
    <div className="gpt3__whatgpt3-container">
      <Feature title="Video is memorable" text="Viewers retain 95% of a video’s message as compared to 10% if reading text." />
      <Feature title="Video grabs attention" text="78% of people watch online videos weekly, and 55% watch videos daily." />
      <Feature title="Video drives action" text="Including videos on your website can increase conversion rates by 80%." />
    </div>
  </div>
);

export default WhatGPT3;
