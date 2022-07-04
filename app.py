from flask import Flask, render_template, url_for, request, redirect

# app instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn_more():
    return render_template('learn.html')

@app.route('/firstregex', methods=["POST", "GET"])
def regex_one():
    
    valid_strings = []
    error_strings = []
    string_validator = "String is Valid."
    error_validator = "String is Not Valid."

    if request.method == "POST":
        # getting input with q1_string_input  in first_regex HTML form
        
        q1_string_input = request.form['q1_string_input']
        s1_string_length = len(q1_string_input)
    
        for char in q1_string_input:
            if char == "a" or char == "b":
                continue
            else:
                error_alphabet = "Please only input a or b."
                return render_template('first_regex.html', error_alphabet=error_alphabet)

        if s1_string_length >= 8:   

            if q1_string_input[-3:] == "aba" or q1_string_input[-3:] == "baa":
                       
                q1_breakdown = q1_string_input[:-3]
                check_valid = "(aba + baa): Valid"
                valid_strings.append(check_valid)
                
                if q1_breakdown[0] == "a" or q1_breakdown[0] == "b":
                        
                    q1_breakdown = q1_breakdown[1:]
                    check_valid_1 = "(a + b): Valid"
                    valid_strings.append(check_valid_1)

                    if "aaab" in q1_breakdown or "bbab" in q1_breakdown or "aaba" in q1_breakdown or "bbba" in q1_breakdown:
                            
                        check_valid_2 = "(aa + bb) (ab + ba): Valid"
                        valid_strings.append(check_valid_2)
                    else:
                        error_message = 'Invalid string for: (aa + bb) (ab + ba)'
                        #string_validator = "String is Valid."
                        error_strings.append(error_message)
                else:
                    error_message_1 = 'Invalid string for: (a + b)'
                    error_strings.append(error_message_1)  
            else:
                error_message_2 = 'Invalid string for: (aba + baa)'
                error_strings.append(error_message_2) 
        else:  
             string_error ='Invalid: Please Input equal or more than 8 characters.'
             return render_template('first_regex.html', string_error=string_error)

    return render_template('first_regex.html', valid_strings=valid_strings, error_strings=error_strings, string_validator=string_validator, error_validator=error_validator)


@app.route('/secondregex', methods=["POST", "GET"])
def regex_two():
    
    valid = []
    error = []
    string_valid = "String is Valid."
    error_valid = "String is Not Valid."

    if request.method == "POST":

        q2_string_input = request.form['q2_string_input']
        s2_string_length = len(q2_string_input)
    
        for char in q2_string_input:
            if char == "0" or char == "1":
                continue
            else:
                error_alphabet = "Please only input 0 or 1."
                return render_template('sec_regex.html', error_alphabet=error_alphabet)

        if s2_string_length >= 5: 

            if q2_string_input[-1] == "0" or q2_string_input[-1] == "1":
                check_valid_4 = "(1 + 0 + 11) Valid"
                valid.append(check_valid_4)

                if q2_string_input[-2:] == "11":
                    q2_breakdown = q2_string_input[:-2]

                else:
                    q2_breakdown = q2_string_input[:-1]

                if q2_breakdown[:2] == "00" or q2_breakdown[:2] == "11":
                    q2_breakdown = q2_breakdown[2:]
                    check_valid = "(aba + baa): Valid"
                    valid.append(check_valid)

                    if "101" in q2_breakdown or "111" in q2_breakdown or "01" in q2_breakdown:
                        check_valid_1 = "(aba + baa): Valid"
                        valid.append(check_valid_1)
                    
                    else:
                        error_message = 'Invalid string for: (101 + 111 + 01)'
                        error.append(error_message)
                            
                else:
                    error_message_2 = 'Invalid string for: (11 + 00)'
                    error.append(error_message_2)
                        
            else:
                error_message_3 = 'Invalid string for: (1 + 0 + 11)'
                error.append(error_message_3)
                    
        else:
            string_error = 'Invalid: Please Input equal or more than 5 characters.'
            return render_template('sec_regex.html', string_error=string_error)
                
    return render_template('sec_regex.html', valid_strings=valid, error_strings=error, string_validator=string_valid, error_validator=error_valid)    


if __name__ == "__main__":
    app.run(debug=True)