var n = prompt('Eneter the number here:')
for(let i = 1; i<=n; i++){
    let output = '';
    for(let j =1; j<=i; j++){
        output += i-j+1;
    }
    console.log(output)
}