
'''
detailed implimentation of the data and adding anf manuplating logics
in json formate

for each of the functionalities it is very very nacessary

go through each page and make it workble formate using save button

project class:
   id

   activities
    add activity
    remove activity
    start date
    end date

    cost:
    total_cost
    transaction_of_costs
    planed_cost

'''

'''
for the prototype verson we are not adding anything into this but we will change the over all system once we move to next phase 
secutity loops need to taken care and store every provious change in server to clear
'''

class Project:

    data={}
    activities=[]


'''
samle code to upload data to server without server

<!DOCTYPE html>
<html>
<head>
    <title>Todo List</title>
</head>
<body>
    <form method="post" id="task-form">
        {% csrf_token %}
        <input type="text" placeholder="Enter Task" name="task" id="task" required>
        <button type="submit">Save</button>
    </form>
  
    <script src="https://code.jquery.com/jquery-3.5.1.js" 
          integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" 
            crossorigin="anonymous"></script>
  
    <script type="text/javascript">
    $(document).on('submit','#task-form',function(e){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'{% url "home" %}',
            data:
            {
                task:$("#task").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                  alert('Saved');
                    }
            })
        });
    </script>
  
</body>
</html>
'''

'''
sample code to load data from server
this will load data after evry 3 second

<script>
    const Story = document.getElementById('stories');
    const Url = '{% url "api" %}/load/{{id}}';

    async function getPosts() {
        await fetch(Url)
            .then((res) => res.json())
            .then((data) => {
                Story.innerHTML = "";
                data.map((post, index) => {
                    Story.innerHTML += `
                <div class="card card-body mb-3">
                  <h3>${post.title}</h3>
                </div>
              `;
                });
            })
            .catch((err) => console.log(err))
    }

    var timer = setInterval(getPosts,3000)
    getPosts();
</script>
'''