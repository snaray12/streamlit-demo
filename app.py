import streamlit as st
from streamlit.components.v1 import html


my_js = '''

<script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" defer></script>
<script>
  window.OneSignal = window.OneSignal || [];
  OneSignal.push(function() {
    OneSignal.init({
      appId: "b7919d51-bfce-4f60-92d6-f339c5abe23c",
    });
  });
</script>
'''

def start_app():
	st.title("Hello World")
	html(my_js)
	st.write("Home Page")


if __name__ == "__main__":
	start_app()