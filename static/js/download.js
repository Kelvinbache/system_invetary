buttom = document.getElementById("Downloads_exel");

buttom.addEventListener("click", async () => {
  try {
    const dataProduct = await fetch("http://127.0.0.1:8080/donwloand");

    if (dataProduct.ok) {
      window.location.href = dataProduct.url;
    }
  } catch (err) {
    return err;
  }
});
