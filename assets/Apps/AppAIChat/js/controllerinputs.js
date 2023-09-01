document.addEventListener("input", function (event) {
    if (
      event.target &&
      event.target.tagName.toLowerCase() === "textarea" &&
      event.target.id === "id-appaichat-input"
    ) {
      event.target.style.height = "60px";
      event.target.style.height = event.target.scrollHeight + "px";
    }
  });


  