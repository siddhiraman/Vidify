import React from 'react';
import Feature from '../../components/feature/Feature';
import './features.css';

const featuresData = [
  {
    title: 'Step 1: Upload your DOC, TXT, or PDF file ',
    text: 'In VidifyPDF choose how you want to create your video - from a text prompt, a link, or an by uploading your PDF documents.',
  },
  {
    title: 'Step 2: Refine your prompt',
    text: 'Next, choose a video template, and adjust your prompt. You can make the prompt more detailed by defining the length, objective, audience, language, speaker, and tone.',
  },
  {
    title: 'Step 3: Edit your video and video script',
    text: 'Once you have the PDF video draft, you can edit every element. You can edit different features.',
  },
  {
    title: 'Step 4: Generate and export your video',
    text: "Click on 'Generate' and your PDF video will be ready in a few minutes. Export it and upload to social media to share it with the world.",
  },
];

const Features = () => (
  <div className="gpt3__features section__padding" id="features">
    <div className="gpt3__features-heading">
      <h1 className="gradient__text">How to convert PDF to video with AI</h1>
    </div>
    <div className="gpt3__features-container">
      {featuresData.map((item, index) => (
        <Feature title={item.title} text={item.text} key={item.title + index} />
      ))}
    </div>
  </div>
);

export default Features;
