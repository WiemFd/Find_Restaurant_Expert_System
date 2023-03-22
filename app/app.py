from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        list =[ request.form.get('customSwitch1', "no"),request.form.get('customSwitch2', "no"),request.form.get('customSwitch3', "no"),request.form.get('customSwitch4', "no")
        ,request.form.get('customSwitch5', "no"),request.form.get('customSwitch6', "no"),request.form.get('customSwitch7', "no"),request.form.get('customSwitch8', "no"),
        request.form.get('customSwitch9', "no"),request.form.get('customSwitch10', "no"),request.form.get('customSwitch11', "no"),request.form.get('customSwitch12', "no"),
        request.form.get('customSwitch13', "no"),request.form.get('customSwitch14', "no"),request.form.get('customSwitch15', "no"),request.form.get('customSwitch16', "no") ]
        print(list)

       
        restaurants = open("restaurants.txt") 
        restaurants_t = restaurants.read() 
        restaurants_list = restaurants_t.split("\n") 
        restaurants.close() 

        for res in restaurants_list: 

            resto_s_file = open("criteria/" + res + ".txt")
            resto_s_data = resto_s_file.read()
            list2 = resto_s_data.split("\n") 
            resto_s_file.close() 
            if list2 == list:
                print(res)
                break
        return render_template(res+'.html')
    return render_template('index.html')

if __name__ == '__main__': 
	app.run(debug=True) 