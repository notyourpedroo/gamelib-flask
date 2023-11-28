$('form input[type="file"]').change(event => {
  let files = event.target.files;
  if (files.length === 0) {
    console.log('No image to show')
  } else {
      if(files[0].type == 'image/jpeg' || files[0].type == 'image/png') {
        $('img').remove();
        let image = $('<img class="img-fluid">');
        image.attr('src', window.URL.createObjectURL(files[0]));
        $('figure').prepend(image);
      } else {
        alert('Format not supported')
      }
  }
});
