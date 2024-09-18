import Image from "next/image";
import React from "react";
import { Button } from "./ui/button";

const LandingPage = () => {
  return (
    <section className="bg-[#062427]">
      <div className="section-container flex flex-col text-white md:flex-row items-center">
        {/* Left Column displaying discription */}
        <div className="flex flex-col mb-32 space-y-12 text-center md:w-1/2 md:text-left">
          {/* Header for Chatting with ResumeGenie*/}
          <h1 className="max-w-md text-4xl md:text-5xl md:leading-tight">
            Uplock Your Career Potential with ResumeGenie
          </h1>

          {/* Description */}
          <p className="max-w-md md:max-w-sm text-white/80 font-light leading-7">
            Get your resume reviewed by our AI-powered resume assistant. Get
            instant feedback on your resume and improve it.
          </p>

          {/* CTA */}
          <div>
            {/* Button */}
            <div className="flex justify-center md:justify-start">
              <Button variant="orange" size="lg">
                Get Started for free
              </Button>
            </div>

            {/* Customers */}
            <div className="flex justify-start mt-6 items-center">
              <Image
                src="/user_1.jpeg"
                alt="Customers"
                width={20}
                height={20}
                className="rounded-full my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/user_2.jpeg"
                alt="Customers"
                width={20}
                height={20}
                className="rounded-full my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/user_3.jpeg"
                alt="Customers"
                width={20}
                height={20}
                className="rounded-full my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/user_4.jpeg"
                alt="Customers"
                width={20}
                height={20}
                className="rounded-full my-auto object-cover ring-2 ring-green-950"
              />
              <Image
                src="/user_5.jpeg"
                alt="Customers"
                width={20}
                height={20}
                className="rounded-full my-auto object-cover ring-2 ring-green-950"
              />
              <div className="flex flex-col md:flex-row md:justify-center md:items-center ml-2">
                <p className="ml-2 my-auto text-sm text-slate-400">
                  Loved by 100,000+ happy users
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column displaying Image */}
        <div className="md:block hidden">
          <Image src="hero2.svg" alt="Hero Image" width={600} height={600} />
        </div>
      </div>
    </section>
  );
};

export default LandingPage;
