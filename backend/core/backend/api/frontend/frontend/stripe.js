async function loadMetrics() {

  const res = await fetch("https://YOUR-API.onrender.com/metrics");
  const data = await res.json();

  document.getElementById("mrr").innerText = data.MRR + " USDC";
  document.getElementById("arr").innerText = data.ARR + " USDC";
  document.getElementById("revenue").innerText = data.total_revenue + " USDC";
  document.getElementById("arpu").innerText = data.ARPU;
  document.getElementById("users").innerText = data.active_users;

  document.getElementById("decisions").innerText =
    JSON.stringify(data.decisions, null, 2);

  let events = "";

  data.events.forEach(e => {
    events += `
💰 ${e.amount} USDC
🧠 ${e.decision}
👤 ${e.user}
⏱ ${e.time}
---
`;
  });

  document.getElementById("events").innerText = events;
}

setInterval(loadMetrics, 3000);
loadMetrics();
