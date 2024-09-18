"use client";
import Image from "next/image";
import React from "react";
import { Button } from "./ui/button";
import { BookOpenCheck, Facebook, Linkedin, Twitter } from "lucide-react";
import TypewriterComponent from 'typewriter-effect';

const LandingPage = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="bg-[#062427]">
        <div className="section-container flex flex-col text-white md:flex-row items-center">
          {/* Left Column displaying discription */}
          <div className="flex flex-col mb-32 space-y-12 text-center md:w-1/2 md:text-left">
            {/* Header for Chatting with ResumeGenie*/}
            <h1 className="max-w-md text-4xl font-medium md:text-5xl md:leading-tight">
              Unlock Your Career Potential with ResumeGenie
            </h1>

            {/* Typewriter effect */}
            <div className="text-3xl font-light text-orange-400">
              <TypewriterComponent
                options={{
                  strings: ['Get Instant Feedback', 'Improve Your Resume', 'Get Hired Faster!'],
                  autoStart: true,
                  loop: true,
                }}
              />
            </div>

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

      {/* Features Section */}
      <section>
        <div className="section-container flex flex-col items-center space-y-12">
          {/* Header */}
          <h2 className="text-4xl text-center font-semibold mb-5 sm:mb-10">
            Features
          </h2>

          {/* Features */}
          <div className="text-black grid grid-cols-1 md:grid-cols-3 gap-8 sm:grid-cols-2 lg:gap-10">
            {/* Feature 1 */}
            <div className="flex flex-col items-center space-y-4 rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <Image
                src="/feature_1.svg"
                alt="Feature 1"
                width={200}
                height={200}
              />
              <h3 className="text-xl">Upload documents</h3>
              <span className="text-center text-gray-500 text-sm block mt-3">
                Upload your resume and cover letter to get instant feedback.
              </span>
            </div>

            {/* Feature 2 */}
            <div className="flex flex-col items-center space-y-4 rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <Image
                src="/feature_2.svg"
                alt="Feature 2"
                width={200}
                height={200}
              />
              <h3 className="text-xl">Resume Templates</h3>
              <span className="text-center text-gray-500 text-sm block mt-3">
                Choose from a wide range of resume templates to create your
                resume.
              </span>
            </div>

            {/* Feature 3 */}
            <div className="flex flex-col items-center space-y-4 rounded-b-xl px-5 pb-5 pt-3 shadow-lg">
              <Image
                src="/feature_3.svg"
                alt="Feature 3"
                width={200}
                height={200}
              />
              <h3 className="text-xl">Sources Included</h3>
              <span className="text-center text-gray-500 text-sm block mt-3">
                Get suggestions on how to improve your resume from multiple
                sources.
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-container">
        <div className="section-container flex flex-col items-center space-y-12">
          {/* Header */}
          <h2 className="text-4xl text-center font-semibold">Get Started</h2>

          {/* CTA */}
          <div className="flex flex-col items-center space-y-4">
            <p className="text-center text-gray-500 text-sm mb-6">
              Get your resume reviewed by our AI-powered resume assistant. Get
              instant feedback on your resume and improve it. Upload your resume
              and get started for free.
            </p>
            <Button variant="orange" size="lg">
              Get Started for free
            </Button>
          </div>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="bg-[#f8f5ee] py-10">
        <div className="mx-auto max-w-7xl px-8 md:px-6">
          {/* Row 1 */}
          <div className="md:flex md:justify-between">
            {/* Logo */}
            <div className="flex items-start mb-6">
              <BookOpenCheck size={40} className="w-8 h-8 mr-3" />
              <span className="text-xl font-medium">ResumeGenie</span>
            </div>

            {/* Links */}
            <div className="grid grid-cols-3 gap-x-20">
              {/* Col-1 */}
              <div>
                <h2 className="mb-4 text-sm font-medium">Products</h2>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">User Cases</a>
                  <a href="#" className="hover:underline">Chrome extention</a>
                  <a href="#" className="hover:underline">Blog</a>
                  <a href="#" className="hover:underline">FAQ</a>
                </div>
              </div>

              {/* Col-2 */}
              <div>
                <h2 className="mb-4 text-sm font-medium">Resources</h2>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">Learn</a>
                  <a href="#" className="hover:underline">Docs</a>
                  <a href="#" className="hover:underline">Community</a>
                </div>
              </div>

              {/* Col-3 */}
              <div>
                <h2 className="mb-4 text-sm font-medium">Company</h2>
                <div className="flex flex-col text-sm text-gray-400 space-y-2">
                  <a href="#" className="hover:underline">About</a>
                  <a href="#" className="hover:underline">Team</a>

                </div>
              </div>
            </div>
          </div>

          <hr className="my-6 border-gray-300 lg:my-8" />

          {/* Row 2 */}
          <div className="text-sm text-gray-500 sm:flex sm:items-center sm:justify-between">
            <span>
              Copyright &copy; 2024, All Rights
            </span>
            <div className="flex text-2xl space-x-6 sm:justify-center">
              <a href="#">
                <Twitter size={20} className="w-6 h-6" />
              </a>
              <a href="#">
                <Linkedin size={20} className="w-6 h-6" />
              </a>
              <a>
                <Facebook size={20} className="w-6 h-6" />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </>
  );
};

export default LandingPage;
