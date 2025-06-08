import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open("trained_model.pkl",'rb'))
scaler = pickle.load(open("scaler.pkl", 'rb')) 


def website_phishing_function(input_data):
    
    try:
        # Convert to float and check for invalid strings
        input_data = [float(x) for x in input_data]
    except ValueError as e:
        return "Invalid input: All fields must be numeric and not empty."

    input_data_reshaped = np.array(input_data).reshape(1, -1)

    # Assuming scaler is already fitted
    scaled_input_data = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(scaled_input_data)
    print(prediction)

    if (prediction[0] == 0):
        return 'The website is legitimate'
    else:
        return 'The website is phishing'
    

def main():
    st.title("Website Prediction Web App")
    
    
    length_url = st.text_input("Total number of characters in the URL: ")
    length_hostname = st.text_input("Number of characters in the hostname: ")
    ip = st.text_input("Whether URL uses an IP address : ")
    nb_dots = st.text_input("Number of dots: ")
    nb_hyphens = st.text_input("Number of hyphens : ")
    nb_qm = st.text_input("Number of question mark : ")
    nb_slash = st.text_input("Number of slashes : ")
    nb_www = st.text_input("Number of occurrences of www : ")
    ratio_digits_url = st.text_input("Ratio of digits to total characters: ")
    ratio_digits_host = st.text_input("Ratio of digits to total characters in the hostname: ")
    length_words_raw = st.text_input("Total length of raw words: ") 
    char_repeat = st.text_input("Maximum consecutive repeating characters: ")
    shortest_words_raw = st.text_input("Length of the shortest word : ")
    shortest_word_host = st.text_input("Length of the shortest word in the hostname: ")
    shortest_word_path = st.text_input("Length of the shortest word in the path: ")
    longest_words_raw = st.text_input("Length of the longest word: ")
    longest_word_host = st.text_input("Length of the longest word in the hostname: ")
    #longest_word_path = st.text_input("Length of the longest word in the path: ")
    avg_words_raw = st.text_input("Average word length in the URL: ")
    avg_word_host = st.text_input("Average word length in the hostname: ")
    avg_word_path = st.text_input("Average word length in the path: ")
    phish_hints = st.text_input("Number of phishing hint keywords detected: ")
    nb_hyperlinks = st.text_input("Number of hyperlinks on the page: ")
    ratio_intHyperlinks = st.text_input("Ratio of internal hyperlinks: ")
    ratio_extHyperlinks = st.text_input("Ratio of external hyperlinks: ")
    ratio_extRedirection = st.text_input("Ratio of external redirection: ")
    #ratio_extErrors = st.text_input("Ratio of external errors: ")
    links_in_tags = st.text_input("Number of <a> tags containing hyperlinks: ")
    #ratio_intMedia = st.text_input("Ratio of internal media files: ")
    #ratio_extMedia = st.text_input("Ratio of external media files: ")
    safe_anchor = st.text_input("Ratio of anchors linking to safe destinations: ")
    domain_in_title = st.text_input("Whether domain name appears in the title: ")
    domain_with_copyright = st.text_input("Whether copyright info contains domain: ")
    domain_registration_length = st.text_input("Number of days the domain is registered for: ")
    domain_age = st.text_input("Number of days since domain creation: ")
    web_traffic = st.text_input("Website's traffic ranking: ")
    google_index = st.text_input("Whether page is indexed on Google: ")
    page_rank = st.text_input("Importance score of the page: ")
    nb_special_char = st.text_input("Number of special characteristics: ")
    nb_digits=st.text_input("Number of digits in URL:")
    nb_suspicious_words=st.text_input("Number of suspicious words in URL:")
    
    Result=""
    if st.button("Website Phishing Result: "):
        Result= website_phishing_function([length_url,length_hostname,ip,nb_dots,nb_hyphens,nb_qm,nb_slash,nb_www,ratio_digits_url,ratio_digits_host,
        length_words_raw,char_repeat,shortest_words_raw,shortest_word_host,shortest_word_path,longest_words_raw,longest_word_host,avg_words_raw,
        avg_word_host,avg_word_path,phish_hints,nb_hyperlinks,ratio_intHyperlinks,ratio_extHyperlinks,ratio_extRedirection,links_in_tags,
        safe_anchor,domain_in_title,domain_with_copyright,domain_registration_length,domain_age,web_traffic,google_index,page_rank,nb_special_char,
        nb_digits,nb_suspicious_words])
    st.success(Result)
    
    
if __name__=='__main__':
    main()