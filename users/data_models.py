from pydantic import BaseModel, Field, field_validator, ValidationError

class UserRequiredParametrs(BaseModel):
    
    username : str = Field(max_length = 16)
    password : str = Field(max_length = 32)
    email : str = Field(max_length = 32)

    @field_validator('username')
    def valid_username(cls, username : str):
        if len(username) < 8:
            raise ValidationError('username field must have length more than or equal 8')
        return username
    
    @field_validator('password')
    def valid_password(cls, password : str):
        if len(password) < 8:
            raise ValidationError('username field must have length more than or equal 8')
        if password.upper() == password.lower():
            raise ValidationError('password must contain at the least one capital letter')
        if not any((i in '0123456789') for i in password):
            raise ValidationError('password must contain at the least one number')
