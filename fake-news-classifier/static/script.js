function showCheckSection() {
    document.getElementById("home-section").style.display = "none";
    document.getElementById("check-section").style.display = "block";
}

function goBack() {
    document.getElementById("check-section").style.display = "none";
    document.getElementById("home-section").style.display = "block";
}

function checkNews() {
    const articleText = document.getElementById("articleText").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Checking...";

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ article_text: articleText })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = "Error: " + data.error;
        } else {
            const label = data.prediction === 'real' ? "✅ Real News" : "❌ Fake News";
            const confidence = Math.round(data.confidence * 100);
            resultDiv.innerHTML = `${label} (Confidence: ${confidence}%)`;
        }
    })
    .catch(err => {
        resultDiv.innerHTML = "An error occurred: " + err.message;
    });
}
