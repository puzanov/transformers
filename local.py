from transformers import pipeline
from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()

login(token=os.getenv("HUGGINGFACE_TOKEN"))

pipeline = pipeline(task="text-generation", model="google/gemma-3-1b-it")
print(pipeline("the secret to baking a really good cake is "))
print(pipeline("what is the capital of the moon?"))
print(pipeline("7+14=?"))

#pipeline = pipeline(task="summarization", model="google/pegasus-billsum")
#print(pipeline("Section was formerly set out as section 44 of this title. As originally enacted, this section contained two further provisions that 'nothing in this act shall be construed as in any wise affecting the grant of lands made to the State of California by virtue of the act entitled 'An act authorizing a grant to the State of California of the Yosemite Valley, and of the land' embracing the Mariposa Big-Tree Grove, approved June thirtieth, eighteen hundred and sixty-four; or as affecting any bona-fide entry of land made within the limits above described under any law of the United States prior to the approval of this act.' The first quoted provision was omitted from the Code because the land, granted to the state of California pursuant to the Act cite, was receded to the United States. Resolution June 11, 1906, No. 27, accepted the recession."))

# Some weights of PegasusForConditionalGeneration were not initialized from 
# the model checkpoint at google/pegasus-billsum and are newly initialized: 
# ['model.decoder.embed_positions.weight', 'model.encoder.embed_positions.weight']
# You should probably TRAIN this model on a down-stream task to be able to 
# use it for predictions and inference.