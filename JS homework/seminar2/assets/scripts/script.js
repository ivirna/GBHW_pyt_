let flag = true;
function changedColor() {
    // получаем элемент по его id
    let element = document.getElementById("el1");
    // if (flag) {
    //      // добавляем класс fire к элементу
    //     element.classList.add("fire");
    //     flag = false;
    // }
    // else {
    //     // удаляем класс fire у элемента
    //     element.classList.remove("fire");
    //     flag = true;
    // }
    // // вывод в консоль
    // console.log(element);
    // добавление класса, если его нет и, наоборот его удаление, если он есть
    element.classList.toggle("fire"); // classList.contains("fire")
    // меняем текст
    // if ( element.textContent == "Всем привет!") element.textContent = "Пока!";
    // else element.textContent = "Всем привет!";
    element.textContent = element.textContent == "Всем привет!" ? "Пока" : "Всем привет!";

    let allUlElements = document.getElementsByTagName("ul");
    let allLiElements = document.getElementsByTagName("li");
    Array.prototype.forEach.call(allUlElements, element => {
        element.classList.toggle("fire");
    });
    Array.prototype.forEach.call(allLiElements, element => {
        element.classList.toggle("fire");
    });
}   

// получаем элемент по id
let btn = document.getElementById("btn");
// log -> находите квадрат в подсказках и tab
console.log(btn);
// слушаем событие "нажатие" -> работает функция changedColor
btn.addEventListener('click', changedColor);