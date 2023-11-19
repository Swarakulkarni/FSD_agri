import express from "express";
import cors from "cors";
import mongoose from "mongoose";
import bcrypt from "bcrypt";

const app = express();
app.use(express.json());
app.use(express.urlencoded());
app.use(cors());

// Update: Remove the callback from mongoose.connect
mongoose.connect("mongodb://localhost:27017/myLoginRegisterDB", {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => {
        console.log("DB connected");
    })
    .catch((error) => {
        console.error('Error connecting to MongoDB', error);
    });

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
});

// Hash passwords before saving
userSchema.pre("save", async function (next) {
    const user = this;
    if (user.isModified("password")) {
        user.password = await bcrypt.hash(user.password, 10);
    }
    next();
});

const User = new mongoose.model("User", userSchema);

//Routes
app.post("/login", async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await User.findOne({ email: email });
        if (user) {
            const isPasswordValid = await bcrypt.compare(password, user.password);
            if (isPasswordValid) {
                res.send({ message: "Login Successful", user: user });
            } else {
                res.send({ message: "Password didn't match" });
            }
        } else {
            res.send({ message: "User not registered" });
        }
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: "Internal Server Error" });
    }
});

app.post("/register", async (req, res) => {
    const { name, email, password } = req.body;
    try {
        const existingUser = await User.findOne({ email: email });
        if (existingUser) {
            res.send({ message: "User already registered" });
        } else {
            const newUser = new User({
                name,
                email,
                password
            });
            await newUser.save();
            res.send({ message: "Successfully Registered, Please login now." });
        }
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: "Internal Server Error" });
    }
});

app.listen(9002, () => {
    console.log("started at port 9002");
});