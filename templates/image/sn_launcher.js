(function(){
if (window.social_network !== undefined){
social_network();
}
else {
document.body.appendChild(
document.createElement('script')
).src='http://127.0.0.1:8000/static/js/sn.js?r=' +
Math.floor(Math.random()*99999999999999999999);
}
})();