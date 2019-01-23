var assets_dir="/static/assets/";
var app = new Vue({
    el: '#app',
    data: {
        product: "socks",
        product_color: "green",
        product_image_dir: assets_dir,
        product_image_alt: "This is "
    }
});