
document.addEventListener('DOMContentLoaded', function() {
    // Encontra o input da foto de perfil e a imagem de preview
    const fotoPerfilInput = document.getElementById('id_foto_perfil');
    const previewImage = document.getElementById('preview-foto-perfil');
    const originalImageSrc = previewImage ? previewImage.src : '';

    // Só executa se os elementos existirem na página
    if (fotoPerfilInput && previewImage) {
        fotoPerfilInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                // Usa o FileReader para ler o arquivo e gerar uma URL de dados
                const reader = new FileReader();
                reader.onload = function(e) {
                    // Define a URL de dados como o src da imagem de preview
                    previewImage.src = e.target.result;
                };
                reader.readAsDataURL(file);
            } else {
                // Se nenhum arquivo for selecionado, volta para a imagem original
                previewImage.src = originalImageSrc;
            }
        });
    }
});
