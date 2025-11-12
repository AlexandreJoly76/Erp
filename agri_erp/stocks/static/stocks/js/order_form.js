// order_form.js
document.addEventListener("DOMContentLoaded", () => {
  // Récupération du dictionnaire produit → prix injecté dans le template
  const productDataEl = document.getElementById("product-data");
  if (!productDataEl) return;

  const productPrices = JSON.parse(productDataEl.textContent);

  document.querySelectorAll(".ligne-commande").forEach((row) => {
    const productSelect = row.querySelector('select[name$="-produit"]');
    const priceInput = row.querySelector('input[name$="-prix_unitaire"]');

    if (!productSelect || !priceInput) return;

    productSelect.addEventListener("change", (e) => {
      const selectedId = e.target.value;
      const price = productPrices[selectedId];
      if (price !== undefined && price !== "") {
        priceInput.value = parseFloat(price).toFixed(2);
      }
    });

    // Auto-remplissage au chargement si déjà choisi
    const initialId = productSelect.value;
    if (initialId && productPrices[initialId] && !priceInput.value) {
      priceInput.value = parseFloat(productPrices[initialId]).toFixed(2);
    }
  });
});
