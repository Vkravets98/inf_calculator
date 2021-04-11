function summa (a,b){
    return a+b
}
//console.log(summa(3,4))

function x_4(a) {
    return a*4
}
//console.log(x_4(2))

function three(a,b,c){
    return (a+b+c)/3
}
//console.log(three(1,1,1))

function no_elements(){
    return 7
}

//console.log(no_elements())

function ostatok(a){
    return a % 5
}

//console.log(ostatok(8))

function mother_name(){
    num = prompt('Введите число: ')
    if (num <= 34) {
        return 'Вася'
    }
    else {
        return 'Света'
    }
}
//console.log(mother_name())

function two_nums(){
    a = prompt('Введите первое число: ')
    b = prompt("Введите второе число: ")
    a = parseInt(a,10)
    b = parseInt(b,10)
    if (a+b == 5) {
        return (a+b)/2
    }
    else {
        return a+b
    }
}
//console.log(two_nums())

function string(){
    s = prompt('Введите любую строку: ')
    if (s.length<5){
        return s
    }
    else {
        return 'Строка сильно большая, я устал'
    }
}
//console.log(string())

function sravnenie(){
    a = prompt('Введите первое число: ')
    b = prompt("Введите второе число: ")
    a = parseInt(a,10)
    b = parseInt(b,10)
    if (a>b) {
        return a+b
    }
    else {
        return a*b
    }
}
//console.log(sravnenie())

function tabl_umn(){
    a = prompt('Введите первое число')
    b = prompt('Введите второе число')
    c = prompt('Введите результат умножения первого числа на второе')
    a = parseInt(a,10)
    b = parseInt(b,10)
    с = parseInt(c,10)
    if(a*b==c){
        return 'Верно'
    }
    else {
        return 'Неверно'
    }
}
//console.log(tabl_umn())

function sum_of_ls(ls){

    for (var i in ls)
        i += ls[i]
        return i
}
//console.log(sum_of_ls([1,2,3,4]))

function ls_div_two(ls){
    ls_new=[]
    for(var i in ls){
        a = ls[i]/2
        ls_new.push(a)
    }
    return ls_new
}
//console.log(ls_div_two([2,4,6]))