from django.shortcuts import HttpResponse

# Create your views here.
def task_create(request):
    html_response = """
    <h1>Yangi vazifa yaratish</h1>
    <form>
        <label>Vazifa nomi: </label>
        <input type="text">
        <br>
        <br>
        <label>Tavsifi: </label>
        <textarea cols="25" rows="4"></textarea>
        <br>
        <br>
        <label>Muddati: </label>
        <input type="date">
        <br>
        <br>
        <label>Muhimlik darajasi: </label>
        <select type="variant">
            <option selected="selected">Past</option>
            <option>O'rta</option>
            <option>Yuqori</option>
        </select>
        <br>
        <br>
        
        <input type="submit" value="Submit">
    </form> 
    """

    return HttpResponse(html_response)