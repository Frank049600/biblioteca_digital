document.addEventListener('DOMContentLoaded', () => {
    // console.log('a')
    const dropdown = document.querySelector('.dropdown');
    const dropdownContent = document.querySelector('.dropdown-content');

    document.querySelector('.dropbtn').addEventListener('click', () => {
        dropdownContent.classList.toggle('show');
    });

    // Ocultar el dropdown si se hace clic fuera de él
    window.addEventListener('click', (event) => {
        if (!dropdown.contains(event.target)) {
            dropdownContent.classList.remove('show');
        }
    });
});

$('#relacion').on('click', function () {
    $('#admo').toggle('slow');
})

$('#botonpia').on('click', function () {
    $('#pia').toggle('slow');
})