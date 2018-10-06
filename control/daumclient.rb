#!/usr/bin/env ruby

#
# Simple Daum Remote Control Client
# 

require 'socket'
require 'eventmachine'

class String
    def hexdump
        i = 0
        line = []
        res = ''
        self.each_char do |c|
            line << c
            res << i.to_s(16).rjust(8, '0') if i % 16 == 0
            res << ' ' if i % 8 == 0
            res << ' '
            res << c.ord.to_s(16).rjust(2, '0')
            i += 1
            if i %16 == 0
                res << '  |'
                line.each { |c| if (c > ' ' and c < '~'); res << c else res << ' ' end }
                res << "|\n"
                line = []
            end
        end
        if i % 16 != 0
            res << '   ' * (16 - i % 16)
            res << ' ' if i % 16 <= 8
            res << '  |'
            line.each { |c| if (c > ' ' and c < '~'); res << c else res << ' ' end }
            res << '|'
        end
        res
    end
end

class DaumCommand
    ETB = 0x17
    GS  = 0x1d
    ACK = 0x06
    NAK = 0x15
    SOH = 0x01
    
    def initialize
        @payload = ''
        @packet = nil
    end

    def request=(r)
        @payload = r
        @packet = nil
    end

    def build
        @packet = ''
        @packet << 0x01
        @packet << @payload
        @checksum = (@payload.chars.inject(0) { |m, c| m += c.ord } % 100).to_s
        @packet << @checksum[0]
        @packet << @checksum[1]
        @packet << ETB
    end

    def packet
        build unless @packet
        @packet
    end
end

module DaumClient
    def post_init
        c = DaumCommand.new
        c.request = 'L70W'
        puts
        puts "Request:"
        puts c.packet.hexdump
        send_data c.packet
    end

    def receive_data data
        if data[0].ord == DaumCommand::ACK
            type = 'ACK'
        elsif data[0].ord == DaumCommand::SOH
            type = 'SOH'
            EventMachine::stop_event_loop
        else
            type = '???'
        end
        puts
        puts "#{type} Response:"
        puts data.hexdump
    end

    def unbind
        puts "Connection has terminated"
    end
end

hostname = ARGV[0]
if not hostname
    puts "usage: status <hostname>"
    exit 1
end

EventMachine.run {
    EventMachine.connect(hostname, 51955, DaumClient)
}
puts "Event loop has ended."
