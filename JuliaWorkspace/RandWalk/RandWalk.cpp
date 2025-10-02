// RandWalk.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#define _SILENCE_CXX17_CODECVT_HEADER_DEPRECATION_WARNING

#include <iostream>
//#include <fstream>
//#include <sstream>
#include <thread>
#include <string>
#include <vector>
#include <map>
#include <random>
//#include <filesystem>
//#include <locale>
#include <cstdint>
#include <direct.h>

// HOLD(241212)

typedef std::vector<std::string> StrVect;
typedef std::map<std::string, std::string> StrMap;

struct P2
{
	float x;
	float y;
};

struct P4
{
	float x;
	float y;
	float z;
	float w;
};

struct P8
{
	float x;
	float y;
	float z;
	float w;
	float u;
	float v;
	float s;
	float t;
};

void RandTest(uint32_t count)
{
	;
}

void ParseArgs(StrVect& outArgs, StrMap& outKArgs, int argc, char* argv[])
{
	;
}

int main(int argc, char* argv[])
{
	StrVect args;
	StrMap kargs;
	ParseArgs(args, kargs, argc, argv);

	std::random_device rd;
	std::mt19937 mt(rd());
	std::uniform_int_distribution<int32_t> dist(0, 1);

	for (int32_t i = 0; i < 100; ++i)
	{
		std::cout << dist(mt) << std::endl;
	}

	std::vector<P2> results;

	P2& newResult = results.emplace_back();

    std::thread thread_test([&newResult]()
	{
		newResult.x = 1;
		newResult.y = 2;
		std::cout << "thread" << std::endl;
	});

	thread_test.join();

	std::cout << newResult.x << ", " << newResult.y << std::endl;

	// write out the results.

	static const char* outputFileName = "RandWalkOutput.log";
	char curDir[_MAX_PATH] = { 0 };
	 _getcwd(curDir, sizeof(curDir) / sizeof(curDir[0]));

	 std::string outputFilePath = curDir;
	 outputFilePath += "\\";
	 outputFilePath += outputFileName;

	std::cout << outputFilePath << std::endl;

	FILE* outputFile = nullptr;
	fopen_s(&outputFile, outputFilePath.c_str(), "w");
	if (outputFile != nullptr)
	{
		std::string output = "hello, world!";
		fwrite(output.c_str(), sizeof(std::string::value_type), output.size(), outputFile);

		fclose(outputFile);
		outputFile = nullptr;
	}

	std::cout << "###########################" << std::endl;
}

//std::filesystem::path curDir = std::filesystem::current_path();
//curDir /= outputFileName;

//std::locale::global(std::locale("en_US.utf8"));
//auto& f = std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(std::locale());

//std::string curDirStr = std::wstring_convert<>(curDir.native());
