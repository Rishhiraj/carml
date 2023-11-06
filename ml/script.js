function getPrediction() {
    const gender = document.getElementById("gender").value;
    const age = parseInt(document.getElementById("age").value);
    const annualIncome = parseInt(document.getElementById("annualIncome").value);

    // You can make an API request to your Flask server to get predictions
    fetch("/predict", {
        method: "POST",
        body: JSON.stringify({ gender, age, annualIncome }),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("predictionResult").innerText = `Prediction: ${data.prediction}`;
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("predictionResult").innerText = "Error occurred while getting prediction.";
        });
}
