import openai 

# load the environment variable, create a .env file and store your OPENAI_API_KEY in that file
from dotenv import load_dotenv
load_dotenv()

# for openai version < 1
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]

# def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, # this is the degree of randomness of the model's output
#     )
# #     print(str(response.choices[0].message))
#     return response.choices[0].message["content"]

# for openai version > 1
client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo",temperature=0):
    messages = messages
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

# Guidelines for using the prompts
def guidelines(case):
    if case == 1:
        """## Prompting Principles
        - **Principle 1: Write clear and specific instructions**
        - **Principle 2: Give the model time to “think”**

        ### Tactics

        #### Tactic 1: Use delimiters to clearly indicate distinct parts of the input
        - Delimiters can be anything like: ```, \""", < >, `<tag> </tag>`, `:`"""

        text = f"""
        You should express what you want a model to do by \ 
        providing instructions that are as clear and \ 
        specific as you can possibly make them. \ 
        This will guide the model towards the desired output, \ 
        and reduce the chances of receiving irrelevant \ 
        or incorrect responses. Don't confuse writing a \ 
        clear prompt with writing a short prompt. \ 
        In many cases, longer prompts provide more clarity \ 
        and context for the model, which can lead to \ 
        more detailed and relevant outputs.
        """
        prompt = f"""
        Summarize the text delimited by triple backticks \ 
        into a single sentence.
        ```{text}```
        """
        response = get_completion(prompt)
        return response
    
    elif case == 2:
        """#### Tactic 2: Ask for a structured output
            - JSON, HTML"""
                
        prompt = f"""
        Generate a list of three made-up book titles along \ 
        with their authors and genres. 
        Provide them in JSON format with the following keys: 
        book_id, title, author, genre.
        """
        response = get_completion(prompt)
        return response
    
    elif case == 3:
        """#### Tactic 3: Ask the model to check whether conditions are satisfied"""
        text_1 = f"""
        Making a cup of tea is easy! First, you need to get some \ 
        water boiling. While that's happening, \ 
        grab a cup and put a tea bag in it. Once the water is \ 
        hot enough, just pour it over the tea bag. \ 
        Let it sit for a bit so the tea can steep. After a \ 
        few minutes, take out the tea bag. If you \ 
        like, you can add some sugar or milk to taste. \ 
        And that's it! You've got yourself a delicious \ 
        cup of tea to enjoy.
        """
        prompt = f"""
        You will be provided with text delimited by triple quotes. 
        If it contains a sequence of instructions, \ 
        re-write those instructions in the following format:

        Step 1 - ...
        Step 2 - …
        …
        Step N - …

        If the text does not contain a sequence of instructions, \ 
        then simply write \"No steps provided.\"

        \"\"\"{text_1}\"\"\"
        """
        response = get_completion(prompt)
        return response
    
    elif case == 4:
        """ #### Tactic 4: "Few-shot" prompting"""
        prompt = f"""
        Your task is to answer in a consistent style.

        <child>: Teach me about patience.

        <grandparent>: The river that carves the deepest \ 
        valley flows from a modest spring; the \ 
        grandest symphony originates from a single note; \ 
        the most intricate tapestry begins with a solitary thread.

        <child>: Teach me about resilience.
        """
        response = get_completion(prompt)
        return response
    
    elif case == 5:
        """### Principle 2: Give the model time to “think” 

        #### Tactic 1: Specify the steps required to complete a task"""
        text = f"""
        In a charming village, siblings Jack and Jill set out on \ 
        a quest to fetch water from a hilltop \ 
        well. As they climbed, singing joyfully, misfortune \ 
        struck—Jack tripped on a stone and tumbled \ 
        down the hill, with Jill following suit. \ 
        Though slightly battered, the pair returned home to \ 
        comforting embraces. Despite the mishap, \ 
        their adventurous spirits remained undimmed, and they \ 
        continued exploring with delight.
        """
        # example 1
        prompt_1 = f"""
        Perform the following actions: 
        1 - Summarize the following text delimited by triple \
        backticks with 1 sentence.
        2 - Translate the summary into French.
        3 - List each name in the French summary.
        4 - Output a json object that contains the following \
        keys: french_summary, num_names.

        Separate your answers with line breaks.

        Text:
        ```{text}```
        """
        response = get_completion(prompt_1)
        return response
    
    elif case == 6:
        """#### Ask for output in a specified format"""
        prompt_2 = f"""
        Your task is to perform the following actions: 
        1 - Summarize the following text delimited by 
        <> with 1 sentence.
        2 - Translate the summary into French.
        3 - List each name in the French summary.
        4 - Output a json object that contains the 
        following keys: french_summary, num_names.

        Use the following format:
        Text: <text to summarize>
        Summary: <summary>
        Translation: <summary translation>
        Names: <list of names in Italian summary>
        Output JSON: <json with summary and num_names>

        Text: <{text}>
        """
        response = get_completion(prompt_2)
        return response
    
    elif case == 7:
        """#### Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion"""
        prompt = f"""
        Determine if the student's solution is correct or not.

        Question:
        I'm building a solar power installation and I need \
        help working out the financials. 
        - Land costs $100 / square foot
        - I can buy solar panels for $250 / square foot
        - I negotiated a contract for maintenance that will cost \ 
        me a flat $100k per year, and an additional $10 / square \
        foot
        What is the total cost for the first year of operations 
        as a function of the number of square feet.

        Student's Solution:
        Let x be the size of the installation in square feet.
        Costs:
        1. Land cost: 100x
        2. Solar panel cost: 250x
        3. Maintenance cost: 100,000 + 100x
        Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
        """
        response = get_completion(prompt)
        return response
    
    elif case == 8:
        """#### Note that the student's solution is actually not correct.
        #### We can fix this by instructing the model to work out its own solution first."""
        prompt = f"""
        Your task is to determine if the student's solution \
        is correct or not.
        To solve the problem do the following:
        - First, work out your own solution to the problem. 
        - Then compare your solution to the student's solution \ 
        and evaluate if the student's solution is correct or not. 
        Don't decide if the student's solution is correct until 
        you have done the problem yourself.

        Use the following format:
        Question:
        ```
        question here
        ```
        Student's solution:
        ```
        student's solution here
        ```
        Actual solution:
        ```
        steps to work out the solution and your solution here
        ```
        Is the student's solution the same as actual solution \
        just calculated:
        ```
        yes or no
        ```
        Student grade:
        ```
        correct or incorrect
        ```

        Question:
        ```
        I'm building a solar power installation and I need help \
        working out the financials. 
        - Land costs $100 / square foot
        - I can buy solar panels for $250 / square foot
        - I negotiated a contract for maintenance that will cost \
        me a flat $100k per year, and an additional $10 / square \
        foot
        What is the total cost for the first year of operations \
        as a function of the number of square feet.
        ``` 
        Student's solution:
        ```
        Let x be the size of the installation in square feet.
        Costs:
        1. Land cost: 100x
        2. Solar panel cost: 250x
        3. Maintenance cost: 100,000 + 100x
        Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
        ```
        Actual solution:
        """
        response = get_completion(prompt)
        return response
    
    elif case == 9:
        """## Model Limitations: Hallucinations
        - Boie is a real company, the product name is not real."""
        prompt = f"""
        Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
        """
        response = get_completion(prompt)
        return response

#Prompting is an iterative process        
def iterative(case):
    #Prompt Engineering, an Iterative Process:
#       a> Try Something
#       b> Analyze where the result does not give what you want.
#       c> Clarify instructions, give more time to think
#       d> Refine prompt with a batch of example
    
    if case == 1:
        """## Generate a marketing product description from a product fact sheet""" 
        fact_sheet_chair = """
        OVERVIEW
        - Part of a beautiful family of mid-century inspired office furniture, 
        including filing cabinets, desks, bookcases, meeting tables, and more.
        - Several options of shell color and base finishes.
        - Available with plastic back and front upholstery (SWC-100) 
        or full upholstery (SWC-110) in 10 fabric and 6 leather options.
        - Base finish options are: stainless steel, matte black, 
        gloss white, or chrome.
        - Chair is available with or without armrests.
        - Suitable for home or business settings.
        - Qualified for contract use.

        CONSTRUCTION
        - 5-wheel plastic coated aluminum base.
        - Pneumatic chair adjust for easy raise/lower action.

        DIMENSIONS
        - WIDTH 53 CM | 20.87”
        - DEPTH 51 CM | 20.08”
        - HEIGHT 80 CM | 31.50”
        - SEAT HEIGHT 44 CM | 17.32”
        - SEAT DEPTH 41 CM | 16.14”

        OPTIONS
        - Soft or hard-floor caster options.
        - Two choices of seat foam densities: 
        medium (1.8 lb/ft3) or high (2.8 lb/ft3)
        - Armless or 8 position PU armrests 

        MATERIALS
        SHELL BASE GLIDER
        - Cast Aluminum with modified nylon PA6/PA66 coating.
        - Shell thickness: 10 mm.
        SEAT
        - HD36 foam

        COUNTRY OF ORIGIN
        - Italy
        """
        prompt = f"""
        Your task is to help a marketing team create a 
        description for a retail website of a product based 
        on a technical fact sheet.

        Write a product description based on the information 
        provided in the technical specifications delimited by 
        triple backticks.

        Technical specifications: ```{fact_sheet_chair}```
        """
        response = get_completion(prompt)
        return response

    elif case == 2:
        """## Issue 1: The text is too long 
        - Limit the number of words/sentences/characters.""" 
        prompt = f"""
        Your task is to help a marketing team create a 
        description for a retail website of a product based 
        on a technical fact sheet.

        Write a product description based on the information 
        provided in the technical specifications delimited by 
        triple backticks.

        Use at most 50 words.

        Technical specifications: ```{fact_sheet_chair}```
        """
        response = get_completion(prompt)
        return response
    
    elif case == 3:
        """## Issue 2. Text focuses on the wrong details
        - Ask it to focus on the aspects that are relevant to the intended audience."""
        prompt = f"""
        Your task is to help a marketing team create a 
        description for a retail website of a product based 
        on a technical fact sheet.

        Write a product description based on the information 
        provided in the technical specifications delimited by 
        triple backticks.

        The description is intended for furniture retailers, 
        so should be technical in nature and focus on the 
        materials the product is constructed from.

        Use at most 50 words.

        Technical specifications: ```{fact_sheet_chair}```
        """
        response = get_completion(prompt)
        return response
    
    elif case == 4:
        """## Issue 3. Description needs a table of dimensions
        - Ask it to extract information and organize it in a table."""

        prompt = f"""
        Your task is to help a marketing team create a 
        description for a retail website of a product based 
        on a technical fact sheet.

        Write a product description based on the information 
        provided in the technical specifications delimited by 
        triple backticks.

        The description is intended for furniture retailers, 
        so should be technical in nature and focus on the 
        materials the product is constructed from.

        At the end of the description, include every 7-character 
        Product ID in the technical specification.

        After the description, include a table that gives the 
        product's dimensions. The table should have two columns.
        In the first column include the name of the dimension. 
        In the second column include the measurements in inches only.

        Give the table the title 'Product Dimensions'.

        Format everything as HTML that can be used in a website. 
        Place the description in a <div> element.

        Technical specifications: ```{fact_sheet_chair}```
        """
        ## Load Python libraries to view HTML
        # from IPython.display import display, HTML
        # display(HTML(response))

        response = get_completion(prompt)
        return response

#Summarizing text
def summarizing(case):
    if case == 1:
        #Text to summarize ,Summarize with a word/sentence/character limit    
        prod_review = """
            Got this panda plush toy for my daughter's birthday, \
            who loves it and takes it everywhere. It's soft and \ 
            super cute, and its face has a friendly look. It's \ 
            a bit small for what I paid though. I think there \ 
            might be other options that are bigger for the \ 
            same price. It arrived a day earlier than expected, \ 
            so I got to play with it myself before I gave it \ 
            to her.
            """   
        prompt = f"""
            Your task is to generate a short summary of a product \
            review from an ecommerce site. 

            Summarize the review below, delimited by triple 
            backticks, in at most 10 words. 

            Review: ```{prod_review}```
            """

        response = get_completion(prompt)
        return response
    
#Infering
def infering(case):
    #Sentiment Analysis
    if case ==1:
        lamp_review = """
            Needed a nice lamp for my bedroom, and this one had \
            additional storage and not too high of a price point. \
            Got it fast.  The string to our lamp broke during the \
            transit and the company happily sent over a new one. \
            Came within a few days as well. It was easy to put \
            together.  I had a missing part, so I contacted their \
            support and they very quickly got me the missing piece! \
            Lumina seems to me to be a great company that cares \
            about their customers and products!!
            """
        prompt = f"""
        What is the sentiment of the following product review, 
        which is delimited with triple backticks?

        Review text: '''{lamp_review}'''
        """
        response = get_completion(prompt)
        return response

    #Extract product and company name from customer reviews¶    
    if case == 2:
        lamp_review = """
            Needed a nice lamp for my bedroom, and this one had \
            additional storage and not too high of a price point. \
            Got it fast.  The string to our lamp broke during the \
            transit and the company happily sent over a new one. \
            Came within a few days as well. It was easy to put \
            together.  I had a missing part, so I contacted their \
            support and they very quickly got me the missing piece! \
            Lumina seems to me to be a great company that cares \
            about their customers and products!!
            """
        prompt = f"""
        Identify the following items from the review text: 
        - Item purchased by reviewer
        - Company that made the item

        The review is delimited with triple backticks. \
        Format your response as a JSON object with \
        "Item" and "Brand" as the keys. 
        If the information isn't present, use "unknown" \
        as the value.
        Make your response as short as possible.
        
        Review text: '''{lamp_review}'''
        """
        response = get_completion(prompt)
        return response

    #Doing multiple tasks at once
    if case==3:
        lamp_review = """
            Needed a nice lamp for my bedroom, and this one had \
            additional storage and not too high of a price point. \
            Got it fast.  The string to our lamp broke during the \
            transit and the company happily sent over a new one. \
            Came within a few days as well. It was easy to put \
            together.  I had a missing part, so I contacted their \
            support and they very quickly got me the missing piece! \
            Lumina seems to me to be a great company that cares \
            about their customers and products!!
            """
        prompt = f"""
        Identify the following items from the review text: 
        - Sentiment (positive or negative)
        - Is the reviewer expressing anger? (true or false)
        - Item purchased by reviewer
        - Company that made the item

        The review is delimited with triple backticks. \
        Format your response as a JSON object with \
        "Sentiment", "Anger", "Item" and "Brand" as the keys.
        If the information isn't present, use "unknown" \
        as the value.
        Make your response as short as possible.
        Format the Anger value as a boolean.

        Review text: '''{lamp_review}'''
        """
        response = get_completion(prompt)
        return response
        
    #Inferring Topics
    if case == 4:
        story = """
        In a recent survey conducted by the government, 
        public sector employees were asked to rate their level 
        of satisfaction with the department they work at. 
        The results revealed that NASA was the most popular 
        department with a satisfaction rating of 95%.

        One NASA employee, John Smith, commented on the findings, 
        stating, "I'm not surprised that NASA came out on top. 
        It's a great place to work with amazing people and 
        incredible opportunities. I'm proud to be a part of 
        such an innovative organization."

        The results were also welcomed by NASA's management team, 
        with Director Tom Johnson stating, "We are thrilled to 
        hear that our employees are satisfied with their work at NASA. 
        We have a talented and dedicated team who work tirelessly 
        to achieve our goals, and it's fantastic to see that their 
        hard work is paying off."

        The survey also revealed that the 
        Social Security Administration had the lowest satisfaction 
        rating, with only 45% of employees indicating they were 
        satisfied with their job. The government has pledged to 
        address the concerns raised by employees in the survey and 
        work towards improving job satisfaction across all departments.
        """    

        prompt = f"""
        Determine five topics that are being discussed in the \
        following text, which is delimited by triple backticks.

        Make each item one or two words long. 

        Format your response as a list of items separated by commas.

        Text sample: '''{story}'''
        """
        response = get_completion(prompt)
        return response

def transforming(case):
    #we will explore how to use Large Language Models for text transformation tasks such as language translation, spelling and grammar checking, tone adjustment, and format conversion.
    if case == 1:
        #ChatGPT is trained with sources in many languages. This gives the model the ability to do translation.
        prompt = f"""
                Translate the following English text to Spanish: \ 
                ```Hi, I would like to order a blender```
                """
        response = get_completion(prompt)
        return response
    
    if case == 2:
        #Universal translator
        user_messages = [
                        "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
                        "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
                        "Il mio mouse non funziona",                                 # My mouse is not working
                        "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
                        "我的屏幕在闪烁"                                               # My screen is flashing
                        ] 
        for issue in user_messages:
            prompt = f"Tell me what language this is: ```{issue}```"
            lang = get_completion(prompt)
            print(f"Original message ({lang}): {issue}")

            prompt = f"""
            Translate the following  text to English \
            and Korean: ```{issue}```
            """
            response = get_completion(prompt)
            print(response, "\n")

    if case == 3:
        #Tone Transformation
        prompt = f"""
        Translate the following from slang to a business letter: 
        'Dude, This is Joe, check out this spec on this standing lamp.'
        """
        response = get_completion(prompt)
        return response

    if case == 4:
        #Format Conversion
        #ChatGPT can translate between formats. The prompt should describe the input and output formats.        
        data_json = { "resturant employees" :[ 
            {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
            {"name":"Bob", "email":"bob32@gmail.com"},
            {"name":"Jai", "email":"jai87@gmail.com"}
        ]}

        prompt = f"""
        Translate the following python dictionary from JSON to an HTML \
        table with column headers and title: {data_json}
        """
        response = get_completion(prompt)
        return response
        #from IPython.display import display, Markdown, Latex, HTML, JSON
        #display(HTML(response))
    
    if case == 5:
        #Spellcheck/Grammar check.
        text = [ 
            "The girl with the black and white puppies have a ball.",  # The girl has a ball.
            "Yolanda has her notebook.", # ok
            "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
            "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
            "Your going to need you’re notebook.",  # Homonyms
            "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
            "This phrase is to cherck chatGPT for speling abilitty"  # spelling
            ]
        for t in text:
            prompt = f"""Proofread and correct the following text
            and rewrite the corrected version. If you don't find
            and errors, just say "No errors found". Don't use 
            any punctuation around the text:
            ```{t}```"""
            response = get_completion(prompt)
            return response
    if case == 6:
        text = f"""
        Got this for my daughter for her birthday cuz she keeps taking \
        mine from my room.  Yes, adults also like pandas too.  She takes \
        it everywhere with her, and it's super soft and cute.  One of the \
        ears is a bit lower than the other, and I don't think that was \
        designed to be asymmetrical. It's a bit small for what I paid for it \
        though. I think there might be other options that are bigger for \
        the same price.  It arrived a day earlier than expected, so I got \
        to play with it myself before I gave it to my daughter.
        """
        prompt = f"proofread and correct this review: ```{text}```"
        response = get_completion(prompt)
        print(response)    
        # from redlines import Redlines

        # diff = Redlines(text,response)
        # display(Markdown(diff.output_markdown))

def expanding(case):
    #Customize the automated reply to a customer email
    # given the sentiment from the lesson on "inferring",
# and the original customer message, customize the email
    sentiment = "negative"

    # review for a blender
    review = f"""
    So, they still had the 17 piece system on seasonal \
    sale for around $49 in the month of November, about \
    half off, but for some reason (call it price gouging) \
    around the second week of December the prices all went \
    up to about anywhere from between $70-$89 for the same \
    system. And the 11 piece system went up around $10 or \
    so in price also from the earlier sale price of $29. \
    So it looks okay, but if you look at the base, the part \
    where the blade locks into place doesn’t look as good \
    as in previous editions from a few years ago, but I \
    plan to be very gentle with it (example, I crush \
    very hard items like beans, ice, rice, etc. in the \ 
    blender first then pulverize them in the serving size \
    I want in the blender then switch to the whipping \
    blade for a finer flour, and use the cross cutting blade \
    first when making smoothies, then use the flat blade \
    if I need them finer/less pulpy). Special tip when making \
    smoothies, finely cut and freeze the fruits and \
    vegetables (if using spinach-lightly stew soften the \ 
    spinach then freeze until ready for use-and if making \
    sorbet, use a small to medium sized food processor) \ 
    that you plan to use that way you can avoid adding so \
    much ice if at all-when making your smoothie. \
    After about a year, the motor was making a funny noise. \
    I called customer service but the warranty expired \
    already, so I had to buy another one. FYI: The overall \
    quality has gone done in these types of products, so \
    they are kind of counting on brand recognition and \
    consumer loyalty to maintain sales. Got it in about \
    two days.
    """      
    prompt = f"""
    You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email delimited by ```, \
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for \
    their review.
    If the sentiment is negative, apologize and suggest that \
    they can reach out to customer service. 
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: ```{review}```
    Review sentiment: {sentiment}
    """
    response = get_completion(prompt)
    return response  

def chatbot(case):
    if case == 1:
        messages =  [  
        {'role':'system', 'content':'You are friendly chatbot.'},
        {'role':'user', 'content':'Hi, my name is Isa'},
        {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
        Is there anything I can help you with today?"},
        {'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
        response = get_completion_from_messages(messages, temperature=1)
        return response
    
if __name__ == "__main__":
    print(chatbot(1))
    
  

   
