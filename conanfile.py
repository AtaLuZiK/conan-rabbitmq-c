from conans import ConanFile, CMake, tools


class RabbitmqcConan(ConanFile):
    name = "rabbitmq-c"
    version = "0.9.0"
    license = "https://github.com/alanxz/rabbitmq-c/blob/v0.9.0/LICENSE-MIT"
    url = "https://github.com/AtaLuZiK/conan-rabbitmq-c.git"
    description = "RabbitMQ C client"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],    # Build rabbitmq-c as a shared library
        "ssl": [True, False],       # Enable SSL support
    }
    default_options = (
        "shared=False",
        "ssl=True",
    )
    requires = "OpenSSL/1.0.2o@conan/stable"
    exports = ["CMakeLists.txt.patch"]
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/alanxz/rabbitmq-c.git")
        self.run("cd %s && git checkout v%s" % (self.name, self.version))
        tools.patch(self.name, "CMakeLists.txt.patch")

    def build(self):
        cmake = CMake(self)
        # Configure
        command_line = [
            cmake.command_line,
            self.cmake_option_bool("ssl", "ENABLE_SSL_SUPPORT"),
            "-DCMAKE_INSTALL_PREFIX:PATH=%s/_" % self.install_folder,
        ]
        self.run("cmake %s %s" % (self.name, " ".join(command_line)))
        cmake.build()
        self.run("cmake --build . --target install")

    def package(self):
        self.copy("config.h", dst="include", src="librabbitmq")
        self.copy("*.h", dst="include", src="_/include")
        self.copy("*.lib", dst="lib", src="_/lib")
        self.copy("*.a", dst="lib", src="_/lib")
        self.copy("*.so", dst="lib", src="_/lib")

    def package_info(self):
        self.cpp_info.libs = ["librabbitmq.4"]

    def cmake_option_bool(self, name, cmake_name):
        return "-D%s=%s" % (cmake_name, ("ON" if getattr(self.options, name) else "OFF"))
