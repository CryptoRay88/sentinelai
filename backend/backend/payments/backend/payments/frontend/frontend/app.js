async function runTest() {

  const res = await fetch("https://YOUR-APP.onrender.com/agent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      login_attempts: Math.floor(Math.random() * 10),
      unusual_ip: true,
      geo_mismatch: true,
      wallet_id: "user_001",
      amount: 0.01,
      intent: "dashboard_test"
    })
  });

  const data = await res.json();

  document.getElementById("output").innerText =
    "🧠 GEMINI RESPONSE:\n" +
    JSON.stringify(data, null, 2);
}
