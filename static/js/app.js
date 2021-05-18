function navToggle() {
  document.getElementById('navbar').classList.toggle('expanded-nav')
  document.getElementById('navbar').classList.toggle('small-nav')
  console.log('hello');
}
var currentCard = 0;
function expandCard(id) {
    console.log('entered');

    if (currentCard == id) {
        document.getElementById(currentCard).classList.toggle('small_height_card');
        var btnId = 'btn' + currentCard
        document.getElementById(btnId).innerHTML = '+'
        console.log('closed');
        currentCard = 0

        return;
    }
    
    if(currentCard != 0){
        document.getElementById(currentCard).classList.toggle('small_height_card');
        var btnId = 'btn' + currentCard
        document.getElementById(btnId).innerHTML = '+'
        console.log('closed');
    }
    
    document.getElementById(id).classList.toggle('small_height_card')
    currentCard = id;
    var btnId = 'btn' + id
    document.getElementById(btnId).innerHTML = '-'

    console.log('opened');

}