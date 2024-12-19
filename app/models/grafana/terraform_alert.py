from typing import Optional, List
from pydantic import BaseModel,PrivateAttr,Field

class ContactPoint(BaseModel):
    use_email:bool = True
    use_slack:bool = True
class GrafanaTerraform(BaseModel):
    create_contact_point:Optional[ContactPoint]
    create_message_template:bool = True
    create_mute_timing:bool = True
    create_notification_policy:bool = True
    
    
