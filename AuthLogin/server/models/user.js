const mongoose = require('mongoose');
const jwt = require('jsonwebtoken');
const Joi = require('joi');
const passwordComplexity = require('joi-password-complexity');
const userSchema = new  mongoose.Schema({
    firstName: {
        type: String,
        required: true,
        min: 3,
        max: 40
    },
    lastName: {
        type: String,
        required: true,
        min: 3,
        max: 40
    },
    email: {
        type: String,
        required: true,
        max: 100
    },
    password: {
        type: String,
        required: true,
        min: 7,
        max: 1024
    },
});

userSchema.methods.generateAuthToken = function() {
    const token = jwt.sign({_id: this._id}, process.env.JWTOKEN, {expiresIn: '7d'});
    return token;
}

const User = mongoose.model('user', userSchema);
const validate = (data) => {
    const schema = Joi.object({
        firstName: Joi.string().min(3).max(40).required().label('First Name'),
        lastName: Joi.string().min(3).max(40).required().label('Last Name'),
        email: Joi.string().max(100).required().email().label('Email'),
        password: passwordComplexity().required().label('Password').min(7).max(1024)
    });
    return schema.validate(data);
}
module.exports = {User, validate};