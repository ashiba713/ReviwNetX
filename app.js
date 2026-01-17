async function upload() {
  const fileInput = document.getElementById("fileInput");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}
