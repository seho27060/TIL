package com.practice.prac1.Controller;


import com.practice.prac1.Domain.DTO.MemberReqDTO;
import com.practice.prac1.Domain.DTO.MemberResDTO;
import com.practice.prac1.Service.MemberService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

    @PostMapping("/save")
    public void saveMember(@RequestBody MemberReqDTO member){
        memberService.saveMember(member);
    }

    @PutMapping("/update/{index}")
    public void updateMember(@PathVariable("index") Long index, @RequestBody MemberReqDTO updatedInput){ memberService.updateMember(index,updatedInput); }

    @DeleteMapping("/delete/{index}")
    public void deleteMember(@PathVariable("index") Long index){memberService.deleteMember(index);}

    @GetMapping("/read/{index}")
    public MemberResDTO readMember(@PathVariable("index") Long index){
        return memberService.readMember(index);
    }
}
