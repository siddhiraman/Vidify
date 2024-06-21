import React, { useState } from 'react';

const UploadPdf = () => {
    const [pdfFile, setPdfFile] = useState(null);
    const [convertedVideoUrl, setConvertedVideoUrl] = useState('');

    const handleFileChange = (e) => {
        setPdfFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('pdf_file', pdfFile);

        try {
            const response = await fetch('http://localhost:5000/upload_pdf', {
                method: 'POST',
                body: formData,
            });
            const data = await response.json();
            setConvertedVideoUrl(data.video_url);
        } catch (error) {
            console.error('Error uploading PDF:', error);
        }
    };

    return (
        <div>
            <input type="file" accept=".pdf" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload PDF</button>
            {convertedVideoUrl && (
                <video controls>
                    <source src={convertedVideoUrl} type="video/mp4" />
                    Your browser does not support the video tag.
                </video>
            )}
        </div>
    );
};

export default UploadPdf;
