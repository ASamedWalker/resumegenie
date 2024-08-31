import React from "react";
import Image from "next/image"; // Import the Image component from the appropriate library
import { Button } from "./ui/button";

const LandingPage = () => {
  return (
    <section className="bg-[#062427]">
      <div className="section-container flex flex-col text-white md:flex-row items-center">
        {/* Left Side */}
        <div className="flex flex-col mb-32 space-y-12 text-center md:w-1/2 md:text-left">
          <h1 className="max-w-md text-4xl font-bold md:text-5xl md:leading-tight">
            Unlock Your Career Potential with Resume AI Ginie
          </h1>
          <p className="max-w-md md:max-w-sm text-white/80 font-light leading-7 mt-4">
            An AI-powered resume builder that helps you create a professional
            resume in minutes.
          </p>
          <div className="flex flex-col items-center md:items-start">
            <Button variant="orange">Get Started for free</Button>

            {/* Customers */}
            <div className="mt-6 flex space-x-0">
              <Image
                src="/images/user_1.jpeg"
                width={200}
                height={200}
                alt="User 1"
                className="rounded-full h-6 w-6 my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/images/user_2.jpeg"
                width={200}
                height={200}
                alt="User 1"
                className="rounded-full h-6 w-6 my-auto object-cover ring-2 ring-green-950"
              />{" "}
              <Image
                src="/images/user_3.jpeg"
                width={200}
                height={200}
                alt="User 1"
                className="rounded-full h-6 w-6 my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/images/user_4.jpeg"
                width={200}
                height={200}
                alt="User 1"
                className="rounded-full h-6 w-6 my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/images/user_5.jpeg"
                width={200}
                height={200}
                alt="User 1"
                className="rounded-full h-6 w-6 my-auto object-cover ring-2 ring-green-950"
              />
              <p className="ml-2 my-auto text-sm text-slate-400">
                Loved by <span className="font-bold">1000+</span> customers
              </p>
            </div>
          </div>
        </div>

        {/* Right Side */}
        <div className="hidden md:block md:w-1/2">
          <Image
            src="/images/hero.svg"
            width={500}
            height={500}
            alt="Hero Image"
            className="w-full"
          />
        </div>
      </div>
    </section>
  );
};

export default LandingPage;
