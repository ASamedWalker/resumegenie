"use client";
import React from "react";
import Image from "next/image"; // Import the Image component from the appropriate library
import { Button } from "./ui/button";
import { BookOpenCheck, Twitter, Facebook, Linkedin } from "lucide-react";
import TypewriterComponent from "typewriter-effect";

const LandingPage = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="bg-[#062427]">
        <div className="section-container flex flex-col text-white md:flex-row items-center">
          {/* Left Side */}
          <div className="flex flex-col mb-32 space-y-12 text-center md:w-1/2 md:text-left">
            <h1 className="max-w-md text-4xl font-bold md:text-5xl md:leading-tight">
              Unlock Your Career Potential with Resume AI Ginie
            </h1>

            <div className="text-3xl font-light text-orange-400">
              <TypewriterComponent
                options={{
                  strings: [
                    "Create a professional resume",
                    "Get your dream job",
                    "Land your dream job",
                    "Get hired",
                  ],
                  autoStart: true,
                  loop: true,
                  deleteSpeed: 50,
                }}
              />
            </div>
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
              priority
            />
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="section-container">
        <h1 className="text-center text-4xl font-semibold mb-5 sm:mb-10">
          How it works
        </h1>
        <div>
          <div className="text-black grid gap-10 sm:grid-cols-2 md:grid-cols-3 lg:gap-10">
            {/* Feature 1 */}
            <div className="rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <div className="flex flex-col items-center justfiy-center">
                <Image
                  src="/images/feature_1.svg"
                  width={200}
                  height={200}
                  alt="Feature 1"
                  style={{width: "auto", height: "auto"}}
                />
              </div>
              <p className="text-center font-medium text-xl mt-5">
                Create a Resume
              </p>
              <span className="block text-sm text-center text-gray-500">
                Create a professional resume in minutes using our AI-powered
                resume builder.
              </span>
            </div>

            {/* Feature 2 */}
            <div className="rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <div className="flex flex-col items-center justfiy-center">
                <Image
                  src="/images/feature_2.svg"
                  width={200}
                  height={200}
                  alt="Feature 2"
                  style={{width: "auto", height: "auto"}}
                />
              </div>
              <p className="text-center font-medium text-xl mt-5">
                Chat with AI Ginie
              </p>
              <span className="block text-sm text-center text-gray-500">
                Get suggestions and recommendations from AI Ginie to improve
                your resume.
              </span>
            </div>

            {/* Feature 3 */}
            <div className="rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <div className="flex flex-col items-center justfiy-center">
                <Image
                  src="/images/feature_3.svg"
                  width={200}
                  height={200}
                  alt="Feature 3"
                  style={{width: "auto", height: "auto"}}
                />
              </div>
              <p className="text-center font-medium text-xl mt-5">Download</p>
              <span className="block text-sm text-center text-gray-500">
                Download your resume in PDF format and start applying for jobs.
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section-container text-center">
        <div className="flex flex-col items-center justify-center">
          <h1 className="text-center text-4xl font-semibold mb-5 sm:mb-10">
            Ready to get started?
          </h1>
          <p className="text-center mt-6 mb-6 text-gray-500">
            Create a professional resume in minutes and land your dream job with
            Resume AI Ginie.
            <br />
            No credit card required.
          </p>
          <div className="w-full max-w sm mx-auto px-4">
            <Button variant="orange">Get Started for free</Button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#f8f5ee] py-10">
        <div className="mx-auto max-w-7xl px-8 md:px-6">
          {/* Row 1 */}
          <div className="md:flex md:justify-between">
            {/* Logo */}
            <div className="flex items-start mb-6">
              <BookOpenCheck className="w-8 h-8 mr-3" size={48} />
              <span className="font-medium text-xl">Resume AI Ginie</span>
            </div>

            {/* Links */}
            <div className="grid grid-cols-3 gap-x-20">
              {/* Col 1 */}
              <div>
                <h3 className="mb-4 text-lg font-medium">Products</h3>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">
                    Resume Builder
                  </a>
                  <a href="#" className="hover:underline">
                    Cover Letter Builder
                  </a>
                  <a href="#" className="hover:underline">
                    Resume Review
                  </a>
                  <a href="#" className="hover:underline">
                    FAQ{" "}
                  </a>
                </div>
              </div>

              {/* Col 2 */}
              <div>
                <h3 className="mb-4 text-lg font-medium">Resources</h3>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">
                    Blog
                  </a>
                  <a href="#" className="hover:underline">
                    Learn
                  </a>
                  <a href="#" className="hover:underline">
                    Doc
                  </a>
                  <a href="#" className="hover:underline">
                    Community
                  </a>
                </div>
              </div>

              {/* Col 3 */}
              <div>
                <h3 className="mb-4 text-lg font-medium">Company</h3>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">
                    About
                  </a>
                  <a href="#" className="hover:underline">
                    Contact
                  </a>
                  <a href="#" className="hover:underline">
                    Careers
                  </a>
                </div>
              </div>
            </div>
          </div>

          <hr className="my-6 border-gray-300 lg:my-8" />

          {/* Row 2 */}
          <div className="text-sm text-gray-500 sm:flex sm:items-center sm:justify-between">
            {/* copy right */}
            <span>
              Copyright &copy; 2024 Resume AI Ginie. All rights reserved.
            </span>
            <div className="flex text-2xl space-x-6 sm:justify-center">
              {/* Social media */}
              <div className="flex textmt-4 space-x-4">
                <a href="#" className="hover:text-gray-900">
                  <Twitter className="w-6 h-6" />
                </a>
                <a href="#" className="hover:text-gray-900">
                  <Linkedin className="w-6 h-6" />
                </a>
                <a href="#" className="hover:text-gray-900">
                  <Facebook className="w-6 h-6" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </>
  );
};

export default LandingPage;
