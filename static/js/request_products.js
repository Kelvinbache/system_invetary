const table = document.getElementById("bodyTable");

document.addEventListener("DOMContentLoaded", async function () {
  load().then((result) => {
    Object.entries(result).forEach(([key, value]) => {
      value.forEach((valuesArray) => {
        const tr = document.createElement("tr");

        valuesArray.forEach((value) => {
          const td = document.createElement("td");
          td.setAttribute("class", "tdTableProducts");
          td.textContent = value;
          tr.appendChild(td);
        });

        table.appendChild(tr);
      });

      addButtom();
    });
  });
});

async function load() {
  try {
    const dataProduct = await fetch("http://127.0.0.1:8080/");
    const result = await dataProduct.json();

    return result;
  } catch (err) {
    return err;
  }
}

function addButtom() {
  const nextElement = table.children;

  for (const next of nextElement) {
    const button = document.createElement("button");
    button.setAttribute("id", "deleteButton");
    button.setAttribute("class", "deleteButton");
    button.textContent = "delete";
    next.appendChild(button);
  }
}
