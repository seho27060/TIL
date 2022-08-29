package com.ssafy.specificPJ.Controller;

import com.ssafy.specificPJ.Domain.DTO.MRDTO;
import com.ssafy.specificPJ.Service.MemberService;
import com.ssafy.specificPJ.Service.SomeService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {

    private final MemberService memberService;

    @PostMapping("/save")
    public void saveMember(@RequestBody MRDTO member){
        memberService.saveMember(member);
    }

    @PutMapping("/update/{index}")
    public void updateMember(@PathVariable Long index, @RequestBody MRDTO member){
        memberService.updateMember(index, member);
    }
}
