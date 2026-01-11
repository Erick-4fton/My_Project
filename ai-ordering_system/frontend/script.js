async function askAI() {
  const input = document.getElementById("userInput").value;
  const result = document.getElementById("result");

  result.innerHTML = "⏳ Memproses...";

  const response = await fetch("http://127.0.0.1:8000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input })
  });

  const data = await response.json();
  result.innerHTML = data.reply;
}
