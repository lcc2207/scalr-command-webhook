# # encoding: utf-8

%w(docker-ce).each do |pkg|
  describe package(pkg) do
    it { should be_installed }
  end
end

%w(command-webhook).each do |container|
  describe docker_container(container) do
    it { should exist }
    it { should be_running }
  end
end

%w(5018).each do |port|
  describe port(port) do
    it { should be_listening }
  end
end

describe pip('docker-compose') do
  it { should be_installed }
end
