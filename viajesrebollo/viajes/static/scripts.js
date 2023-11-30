function toggleDropdownCheckList(id) {
    var list = document.getElementById(id);

    if (!list) {
        console.error("Element with id '" + id + "' not found.");
        return;
    }

    var anchor = list.closest('.dropdown-check-list').querySelector('.anchor');

    if (!anchor) {
        console.error("Anchor element not found.");
        return;
    }

    list.style.display = (list.style.display === "none" || list.style.display === "") ? "block" : "none";
    anchor.classList.toggle('opened', list.style.display === "block");
}
