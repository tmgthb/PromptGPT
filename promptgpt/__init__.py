def gpt_program(gpt_program_input, gpt_program_system, gpt_model, max_length):
    """
        ---Generic GPT Program---
        gpt_program_input: what is the input?
        gpt_program_system: What is your gpt should perform?
        gpt_model: What model to use?
        max_length: What is the total length input + output?
    """
    gpt_program_response = openai.ChatCompletion.create(
        model = gpt_model,
        messages = [
            {"role": "system", "content": f"{gpt_program_system}"},
            {"role": "user", "content": ""},
            {"role": "assistant", "content": "How can I help you?"},
            {"role": "user", "content": f"{gpt_program_input}"},
        ],
        max_tokens=max_length,
        temperature=0)
    gpt_program_output = gpt_program_response['choices'][0]['message']['content']
    return gpt_program_output

def save_memory(memory_input, memory_file):
    """
    ---SAVE MEMORY---
    memory_input: What is text to be stored in the .txt-file?
    memory_file: What variable is used to store the text?
    """
    with open(memory_file, 'w') as f:
        f.write(str(memory_input))
    return memory_file

def get_memory(memory_file, memory):
    """
    ---RETRIEVE MEMORY---
    memory_file: What variable is used to store the text?
    memory: What is the memory variable? 
    """
    with open(memory_file, "r") as f:
        memory = f.read()
    return memory 

def get_task(define_task, define_task_system):
    """
    ---GET TASK---
    What task you want to use?
    What is its system instruction?
    """
    actual_task = ""
    define_task = define_task.format(memory)
    actual_task = gpt_program(define_task, define_task_system, model_to_use, execution_length)
    return actual_task

def get_role(define_role, define_role_system):
    """
    ---GET ROLE---
    What role you want to use?
    What is its system instruction?
    """
    actual_task_role = ""
    define_role = define_role.format(memory)
    actual_task_role = gpt_program(define_role, define_role_system, model_to_use, execution_length)
    return actual_task_role

def get_resource(define_resource, define_resource_system):
    """
    ---GET RESOURCE---
    What resource you want to use?
    What is its system instruction?
    """
    actual_task_resource = ""
    define_resource = define_resource.format(memory)
    actual_task_resource = gpt_program(define_resource, define_resource_system, model_to_use, execution_length)
    return actual_task_resource

def get_task_memory(define_memory, define_memory_system):
    """
    ---GET TASK MEMORY---
    What memory you want to use?
    What is its system instruction?
    """
    actual_task_memory = ""
    define_memory = define_memory.format(memory)
    actual_task_memory = gpt_program(define_memory, define_memory_system, model_to_use, execution_length)
    return actual_task_memory

def execute(execution_script, execution_system_instruction):
    """
    ---EXECUTE A TASK---
    What task you want to execute?
    What is its system instruction?
    """
    execution_output = ""
    execution_system_instruction= execution_system_instruction.format(task_role, task, task_resource)
    execution_output = gpt_program(execution_script, execution_system_instruction, model_to_use, execution_length)
    return execution_output
