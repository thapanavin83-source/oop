from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/prime_number/<int:number>',methods=['GET'])
def isPrime(number):
    if number<2:
        result= False

    else:
        result=True
        for i in range(2, number):
            if number%i==0:
                result= False
                break
    return jsonify({
        "Number":number,
        "isPrime":result
    })

app.run(debug=True)
